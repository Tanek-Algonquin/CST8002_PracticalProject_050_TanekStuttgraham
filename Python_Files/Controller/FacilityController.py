from Model.facilityModel import FacilityModel
from Model.facilityClass import facilityClass

class FacilityController:
    """Facility Controller manipulates the model based on event cues from the view class."""
    def __init__(self, model, view):
        """Initialize the controller with a model and a view."""
        self.model = model
        self.view = view

    def load_facilities(self):
        """Load facilities from DB into the model."""
        self.model.load_all_changed_facilities()
        self.view.update_facility_list()
        
    def load_original_to_changed(self):
        self.model.load_original_to_changed()
        self.view.update_facility_list()
    
    def load_original_facilities(self):
        """Load facilities from DB into the model."""
        self.model.load_original_facilities()
        self.view.update_facility_list()
        
    def load_one_facility(self, facilityId):
        """Loads one facility from CSV into memory"""
        self.model.load_changed_facility_by_id(facilityId)
        self.view.update_facility_list()
            
            
    def save_facilities(self):
        """Save facilities from the model to DB."""
        self.model.save_facilities()

    def add_facility(self, facility_data):
        """Create a new facility from user input and add it to the model."""
        try:
            facility = facilityClass(
                region=facility_data["Region"],
                district=facility_data["District"],
                licenceNum=facility_data["Licence Number"],
                facilityName=facility_data["Facility Name"],
                facilityType=facility_data["Facility Type"],
                facilityAddress1=facility_data["Facility Address 1"],
                facilityAddress2=facility_data["Facility Address 2"],
                facilityAddress3=facility_data["Facility Address 3"],
                maxNumofChildren=int(facility_data["Max Number of Children"]),
                maxNumInfants=int(facility_data["Max Number of Infants"]),
                maxNumPreChildren=int(facility_data["Max-Number-of-Preschool-Aged-Children"]),
                maxNumSAgeChildren=int(facility_data["Max-Number-of-School-Age-Children"]),
                LangOfService=facility_data["Language of Service"],
                operatorId=facility_data["Operator Id"],
                designatedFacility=facility_data["Designated Facility"]
            )
            
            self.model.add_to_changed_facilities(facility)
            self.view.update_facility_list()
        
        except ValueError:
            print("Error: Please enter valid numerical values for child capacities.")
            
    def get_edited_facility_data(self):
        """Retrieve edited facility data from the UI."""
        facility_data = {key: self.edit_fields[key].get() for key in self.edit_fields}
        return facility_data
    
    def get_facility_data(self, index):
        """Retrieve facility data as a dictionary to send to the view."""
        if 0 <= index < len(self.model.record_list):
            facility = self.model.record_list[index]

            return {
                "Region": facility.region,
                "District": facility.district,
                "Licence Number": facility.licenceNum,
                "Facility Name": facility.facilityName,
                "Facility Type": facility.facilityType,
                "Facility Address 1": facility.facilityAddress1,
                "Facility Address 2": facility.facilityAddress2,
                "Facility Address 3": facility.facilityAddress3,
                "Max Number of Children": facility.maxNumofChildren,
                "Max Number of Infants": facility.maxNumInfants,
                "Max-Number-of-Preschool-Aged-Children": facility.maxNumPreChildren,
                "Max-Number-of-School-Age-Children": facility.maxNumSAgeChildren,
                "Language of Service": facility.LangOfService,
                "Operator Id": facility.operatorId,
                "Designated Facility": facility.designatedFacility
            }
        return None
    
    def update_facility(self, index, facility_data):
        """Update an existing facility in the model."""
        if 0 <= index < len(self.model.record_list):
            facility = self.model.record_list[index]

            facility.region = facility_data["Region"]
            facility.district = facility_data["District"]
            facility.licenceNum = facility_data["Licence Number"]
            facility.facilityName = facility_data["Facility Name"]
            facility.facilityType = facility_data["Facility Type"]
            facility.facilityAddress1 = facility_data["Facility Address 1"]
            facility.facilityAddress2 = facility_data["Facility Address 2"]
            facility.facilityAddress3 = facility_data["Facility Address 3"]
            facility.maxNumofChildren = int(facility_data["Max Number of Children"])
            facility.maxNumInfants = int(facility_data["Max Number of Infants"])
            facility.maxNumPreChildren = int(facility_data["Max-Number-of-Preschool-Aged-Children"])
            facility.maxNumSAgeChildren = int(facility_data["Max-Number-of-School-Age-Children"])
            facility.LangOfService = facility_data["Language of Service"]
            facility.operatorId = facility_data["Operator Id"]
            facility.designatedFacility = facility_data["Designated Facility"]

            self.view.update_facility_list()

    def delete_facility(self, facilityId):
        """Delete a facility from the model based on Facility Id."""
        self.model.delete_facility(facilityId)
        self.view.update_facility_list()
        