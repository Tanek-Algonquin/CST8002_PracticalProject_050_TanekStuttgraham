import  mysql.connector
from Model.facilityClass import facilityClass

"""This file (FacilityModel) was written by Tanek Stuttgraham Student No 041012512, Course Code: CST8002_050, Prof. Todd Keuleman"""
class FacilityModel:
    def __init__(self):
        """Initialize FacilityModel with empty record list."""
        self.record_list = []  # List to store facility objects
        self.conn = mysql.connector.connect ( #MySQL Connection.
        host="localhost",
        user="cst8277",
        password="8277",
        database="pythondb"
        )
        self.cursor = self.conn.cursor(dictionary=True)
        
        
    def load_original_to_changed(self):
        """Method loads original facility data to changed facility table to reset the chenged table."""
        try:
            self.cursor.execute("DELETE * FROM changed_childcare_facilities")#Clear table before loading
            self.cursor.execute("""INSERT INTO changed_childcare_facilities SELECT * FROM original_childcare_facilities""")
            
            self.conn.commit()
            print("Loaded original table to changed table.")
            
            except mysql.connector.Error as e:
                print(f"Database Error: {e}")
    
    def load_all_changed_facilities(self):
        """Method loads All records from changed facility table."""
        try:
            self.cursor.execute("SELECT * FROM changed_childcare_facilities")
            self.record_list = self.cursor.fetchall() #Pass records to list.
            return  record_list
        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
            return []
        
    def load_changed_facility_by_id(self, facilityId):
        """Loads A specified changed facility record by its Id"""
            try:
                self.cursor.execute("SELECT FROM changed_childcare_facilities WHERE id = %s", (facilityId))
                return self.cursor.fetchone()
            except mysql.connector.Error as e:
                print(f"DataBaseError: {e}")
                return None #Return Nothing If Error occurs
            
    def add_to_changed_facilities(self, facility):
        """Adds a facility record to Changed childcare facility table."""
         #Prepared Statement
        prepared_sql = """
        INSERT INTO original_childcare_facilities (region, district, licenceNum, facilityName, facilityType,
            facilityAddress1, facilityAddress2, facilityAddress3,
            maxNumofChildren, maxNumInfants, maxNumPreChildren,
            maxNumSAgeChildren, LangOfService, operatorId, designatedFacility)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """

        # Values to insert into the database
        values = (
            region, district, licenceNum, facilityName, facilityType,
            facilityAddress1, facilityAddress2, facilityAddress3,
            maxNumofChildren, maxNumInfants, maxNumPreChildren,
            maxNumSAgeChildren, LangOfService, operatorId, designatedFacility)
        
        self.cursor.execute(prepared_sql, values)
        self.conn.commit()
        print("Facility Added to Changed Facilty Tabke Successfully")
        
    def update_in_changed_facilities(self, facilityid, updatedValues):
        """Updates an existing Facility in Changed Facilites table."""
        if not updatedValues:
            print("No Updated Values Provided.")
            return
        try:
            prepared_sql = f"UPDATE changed_childcare_facilities SET 	{', '.join(f'{k} = %s' for k in updated_values)} WHERE id = %s"
            self.cursor.execute(prepared_sql, (*updatedValues.values(), facilityid))
            self.conn.commit()
            print("Updated Succesfully")
        except mysql.connector.Error as e:
            print("Sql Error : {e} ")
                    

    def delete_facility(self, facilityId):
            """Delete a facility from changed_childcare_facilities."""
            try:
                self.cursor.execute("DELETE FROM changed_childcare_facilities WHERE id = %s", (facilityId,))
                self.conn.commit()
                print("Facility deleted successfully.")
            except mysql.connector.Error as e:
                print(f"Database Error: {e}")
     
            
    def restore_original_facilities(self):
            """Rewrite changed_childcare_facilities with original_childcare_facilities data."""
            self.load_original_facilities()
            print("Restored changed_childcare_facilities to original state.")
        
    
    def close_connection(self):
    """Close the database connection."""
    self.cursor.close()
    self.conn.close()
    
