
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
        
    def get_facility_chart_data(self, column_name):
        """Fetch Column type and counts repeated instances from the record list for plotting."""
        column_counts  = {}

        for facility in self.model.record_list:
            value = getattr(facility, column_name)
            column_counts [value] = column_counts .get(value, 0) + 1  # Count occurrences
        
        # Convert dictionary to lists for plotting
        categories = list(column_counts .keys())
        values = list(column_counts .values())

        return categories, values

        
    def load_original_to_changed(self):
        """Calls on model, load_original_to_changed method. Then calls the view to reflect the change."""
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
        
    def get_changed_facility_by_id(self, facilityId):
        """Fetches a changed facility from the database and returns it to the view."""
        return self.model.load_changed_facility_by_id(facilityId)
            
            
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
            
    def get_first_available_facility(self):
        """Fetch the first available facility and update the view."""
        facility = self.model.get_first_available_facility()
        if facility:
            self.view.update_facility_list()  # Refresh the Treeview
        else:
            self.view.show_message("No facility records found.")
        
    
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
        """Update an existing facility in the model and persist it to the database."""
        if 0 <= index < len(self.model.record_list):
            facility = self.model.record_list[index]

            # Update in-memory record
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

            # Persist changes to the database
            updated_values = {  
                "region": facility.region,
                "district": facility.district,
                "licenceNum": facility.licenceNum,
                "facilityName": facility.facilityName,
                "facilityType": facility.facilityType,
                "facilityAddress1": facility.facilityAddress1,
                "facilityAddress2": facility.facilityAddress2,
                "facilityAddress3": facility.facilityAddress3,
                "maxNumofChildren": facility.maxNumofChildren,
                "maxNumInfants": facility.maxNumInfants,
                "maxNumPreChildren": facility.maxNumPreChildren,
                "maxNumSAgeChildren": facility.maxNumSAgeChildren,
                "LangOfService": facility.LangOfService,
                "operatorId": facility.operatorId,
                "designatedFacility": facility.designatedFacility
            }

            self.model.update_in_changed_facilities(facility.facilityId, updated_values)

            # Refresh the Treeview
            self.view.update_facility_list()

    def delete_facility(self, facilityId):
        """Delete a facility from the model based on Facility Id."""
        self.model.delete_facility(facilityId)
        self.view.update_facility_list()
    
    def delete_changed_facilities(self):
        self.model.delete_changed_facilities()
        self.view.update_facility_list()
        