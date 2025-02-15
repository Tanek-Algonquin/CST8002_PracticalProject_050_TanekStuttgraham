from Model.facilityModel import FacilityModel
from Model.facilityClass import facilityClass

class FacilityController:
    def __init__(self, model, view):
        """Initialize the controller with a model and a view."""
        self.model = model
        self.view = view

    def load_facilities(self):
        """Load facilities from CSV into the model."""
        self.model.load_from_csv()
        self.view.update_facility_list()
        
    def load_one_facility(self, index):
        """Loads one facility from CSV into memory"""
        self.model.load_one_from_csv(index)
        self.view.update_facility_list()
    

    def save_facilities(self):
        """Save facilities from the model to CSV."""
        self.model.save_facilities()

    def add_facility(self, facility_data):
        """Create a new facility from user input and add it to the model."""
        try:
            facility = facilityClass(
                region=facility_data["Region"],
                district=facility_data["District"],
                licenseNum=facility_data["License Number"],
                facilityName=facility_data["Facility Name"],
                facilityType=facility_data["Facility Type"],
                facilityAddress1=facility_data["Facility Address 1"],
                facilityAddress2=facility_data["Facility Address 2"],
                facilityAddress3=facility_data["Facility Address 3"],
                maxNumofChildren=int(facility_data["Max Number of Children"]),
                maxNumInfants=int(facility_data["Max Number of Infants"]),
                maxNumPreChildren=int(facility_data["Max Number of Preschool-Aged Children"]),
                maxNumSAgeChildren=int(facility_data["Max Number of School Age Children"]),
                LangOfService=facility_data["Language of Service"],
                operatorId=facility_data["Operator Id"],
                designatedFacility=facility_data["Designated Facility"]
            )

            self.model.record_list.append(facility)
            self.view.update_facility_list()
        
        except ValueError:
            print("Error: Please enter valid numerical values for child capacities.")
            


    def delete_facility(self, index):
        """Delete a facility from the model based on index."""
        if 0 <= index < len(self.model.record_list):
            del self.model.record_list[index]
            self.view.update_facility_list()
        else:
            print("Invalid index for deletion.")
