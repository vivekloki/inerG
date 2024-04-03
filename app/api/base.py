"""API Endpoints related to Ohio quarterly production data"""

from flask import request, jsonify

from app.api import bp
from app.models import BaseModel
from app.services.organization_service import get_organization_data, get_data_of_single_quarter, get_data_of_multiple_quarters

# @bp.route('/data', methods=['GET'])
# def get_annual_data():
#     api_well_number = request.args.get('well')
#     print(api_well_number)
#     if not api_well_number:
#         return jsonify({'error': 'Well number not provided'}), 400
#     organization = get_organization_data(api_well_number)
#     if not organization:
#         return jsonify({'error': 'Organization not found'}), 404
#     response = {
#         'oil': organization.oil,
#         'gas': organization.gas,
#         'brine': organization.brine
#     }
#     return jsonify({'message': 'Success','data': response, 'status': 200}), 200


@bp.route('/test', methods=['GET'])
def abc():
    response, status_code = BaseModel.load_annual_data_from_csv('inerg_data.csv')
    return response, status_code


@bp.route('/data', methods=['GET'])
def get_annual_data():
    api_well_number = request.args.get('well')
    quarter = request.args.get('quarter')

    # Check if the 'quarter' parameter is provided
    if quarter:
        try:
            # Check if multiple quarters are provided separated by commas
            if ',' in quarter:
                # Split the quarters into a list of integers
                quarters = [int(q) for q in quarter.split(',')]
                # Check for invalid quarters (outside range 1-4)
                invalid_quarters = [q for q in quarters if q < 1 or q > 4]
                # If there are invalid quarters, return an error response
                if invalid_quarters:
                    return jsonify({'error': 'Invalid quarter number'}), 400
                # Call function to get data for multiple quarters
                data = get_data_of_multiple_quarters(quarters, api_well_number)
            else:
                # Convert single quarter parameter to integer
                quarter = int(quarter)
                # Check if the single quarter is within range 1-4
                if quarter < 1 or quarter > 4:
                    # If not, return an error response
                    return jsonify({'error': 'Invalid quarter number'}), 400
                # Call function to get data for a single quarter
                data = get_data_of_single_quarter(quarter, api_well_number)
            # If no data is found, return an error response
            if not data:
                return jsonify({'error': 'Data not found for specified quarter'}), 404
            # Return success response with the retrieved data
            return jsonify({'message': 'Success', 'data': data, 'status': 200}), 200
        # Handle the ValueError exception if the quarter parameter is not a valid integer or comma-separated list
        except ValueError:
            return jsonify({'error': 'Quarter must be an integer or a comma-separated list of integers'}), 400
    # If 'well' parameter is not provided, return an error response
    if not api_well_number:
        return jsonify({'error': 'Well number not provided'}), 400
    # Get organization data based on the provided 'well' number
    organization = get_organization_data(api_well_number)
    # If organization data is not found, return an error response
    if not organization:
        return jsonify({'error': 'Organization not found'}), 404
    response = {
        'oil': organization.oil,
        'gas': organization.gas,
        'brine': organization.brine
    }
    return jsonify({'message': 'Success', 'data': response, 'status': 200}), 200