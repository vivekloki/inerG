from app.models import BaseModel


def get_organization_data(api_well_number):
    """
    Retrieve organization data from the database based on the provided API well number.
    """
    organization = BaseModel.query.filter_by(api_well_number=api_well_number).first()
    return organization
