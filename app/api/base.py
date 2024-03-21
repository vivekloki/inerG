"""API Endpoints related to Ohio quarterly production data"""

from flask import request, jsonify

from app.api import bp
from app.models import BaseModel
from app.services.organization_service import get_organization_data


@bp.route('/data', methods=['GET'])
def get_annual_data():
    api_well_number = request.args.get('well')
    print(api_well_number)
    if not api_well_number:
        return jsonify({'error': 'Well number not provided'}), 400
    organization = get_organization_data(api_well_number)
    if not organization:
        return jsonify({'error': 'Organization not found'}), 404
    response = {
        'oil': organization.oil,
        'gas': organization.gas,
        'brine': organization.brine
    }
    return jsonify({'message': 'Success','data': response, 'status': 200}), 200


@bp.route('/test', methods=['GET'])
def abc():
    response, status_code = BaseModel.load_annual_data_from_csv('inerg_data.csv')
    return response, status_code