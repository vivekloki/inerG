import csv

from app.models import BaseModel
from flask import jsonify
from collections import defaultdict

# def get_organization_data(api_well_number, quarter):
def get_organization_data(api_well_number):
    """
    Retrieve organization data from the database based on the provided API well number.
    """
    organization = BaseModel.query.filter_by(api_well_number=api_well_number).first()
    return organization



def get_data_of_single_quarter(quarter, well_number):
    try:
        with open('inerg_data.csv', 'r') as file:
            reader = csv.DictReader(file)
            quarterly_data = {}
            current_quarter = 0
            for row in reader:
                api_well_number = row.get('API WELL  NUMBER', '')
                if not api_well_number:
                    continue
                if api_well_number != well_number:
                    continue 
                current_quarter += 1
                if current_quarter == quarter:
                    oil = int(row.get('OIL', '0').replace(',', ''))
                    gas = int(row.get('GAS', '0').replace(',', ''))
                    brine = int(row.get('BRINE', '0').replace(',', ''))
                    quarterly_data[api_well_number] = {'OIL': oil, 'GAS': gas, 'BRINE': brine}
                    break
            return quarterly_data
    except FileNotFoundError:
        print("File not found")
        return None


def get_data_of_multiple_quarters(quarters, well_number):
    try:
        with open('inerg_data.csv', 'r') as file:
            reader = csv.DictReader(file)
            quarterly_data = {quarter: {} for quarter in quarters}
            current_quarter = 0
            for row in reader:
                api_well_number = row.get('API WELL  NUMBER', '')
                if not api_well_number:
                    continue

                if api_well_number != well_number:
                    continue  
                current_quarter += 1
                if current_quarter in quarters:
                    oil = int(row.get('OIL', '0').replace(',', ''))
                    gas = int(row.get('GAS', '0').replace(',', ''))
                    brine = int(row.get('BRINE', '0').replace(',', ''))
                    quarterly_data[current_quarter][api_well_number] = {'OIL': oil, 'GAS': gas, 'BRINE': brine}
            return quarterly_data
    except FileNotFoundError:
        print("File not found")
        return None
