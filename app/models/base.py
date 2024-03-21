import csv
from flask import jsonify
from app import db


class BaseModel(db.Model):
    """Table for defining the organization details"""
    __tablename__ = "organization"
    id = db.Column(db.Integer, primary_key=True, index=True)
    api_well_number = db.Column(db.Integer, nullable=True, unique=True)
    oil = db.Column(db.Integer, nullable=True)
    gas = db.Column(db.Integer, nullable=True)
    brine = db.Column(db.Integer, nullable=True)

    def to_dict(self):
        """Convert table object to dictionary."""
        data = dict(
            id=self.id,
            api_well_number=self.api_well_number,
            oil=self.oil,
            gas=self.gas,
            brine=self.brine
        )
        return data

    @staticmethod
    def load_annual_data_from_csv(csv_file):
        try:
            with open(csv_file, 'r') as file:
                reader = csv.DictReader(file)
                annual_data = {}
                for row in reader:
                    api_well_number = row.get('API WELL  NUMBER', '')
                    if not api_well_number:
                        continue
                    oil = int(row.get('OIL', '0').replace(',', ''))
                    gas = int(row.get('GAS', '0').replace(',', ''))
                    brine = int(row.get('BRINE', '0').replace(',', ''))

                    if api_well_number in annual_data:
                        annual_data[api_well_number]['oil'] += oil
                        annual_data[api_well_number]['gas'] += gas
                        annual_data[api_well_number]['brine'] += brine
                    else:
                        annual_data[api_well_number] = {'oil': oil, 'gas': gas, 'brine': brine}

                # Inserting data into the database
                for api_well_number, production in annual_data.items():
                    oil = production['oil']
                    gas = production['gas']
                    brine = production['brine']
                    base_model = BaseModel(api_well_number=api_well_number, oil=oil, gas=gas, brine=brine)
                    db.session.add(base_model)

                # Committing changes to the database
                db.session.commit()
                print("Data successfully inserted into SQLite database.")
                
                # Return a success response
                return jsonify({'message': 'Data insertion successful', 'status': 200}), 200
        except Exception as e:
            # Rollback changes on failure
            db.session.rollback()
            # Return an error response
            return jsonify({'error': str(e), 'status': 500}), 500
