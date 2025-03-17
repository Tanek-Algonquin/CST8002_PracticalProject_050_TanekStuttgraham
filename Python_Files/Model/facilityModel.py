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
            self.cursor.execute("DELETE FROM changed_childcare_facilities")#Clear table before loading
            self.cursor.execute("""INSERT INTO changed_childcare_facilities SELECT * FROM original_childcare_facilities""")
            
            self.conn.commit()
            print("Loaded original table to changed table. Tanek Stuttgraham 041012512")
            
        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
    
    def load_original_facilities(self):
        """Method loads All records from original_childcare_facilities table and converts them to facilityClass instances."""
        try:
            self.cursor.execute("SELECT * FROM original_childcare_facilities")
            rows = self.cursor.fetchall()  # Fetch all rows as dictionaries
            
            # Convert each dictionary into a facilityClass instance
            self.record_list = []
            for row in rows:
          
                facility = facilityClass(
                    
                    facilityId=row["id"],
                    region=row["region"],
                    district=row["district"],
                    licenceNum=row["licenceNum"],
                    facilityName=row["facilityName"],
                    facilityType=row["facilityType"],
                    facilityAddress1=row["facilityAddress1"],
                    facilityAddress2=row["facilityAddress2"],
                    facilityAddress3=row["facilityAddress3"],
                    maxNumofChildren=row["maxNumofChildren"],
                    maxNumInfants=row["maxNumInfants"],
                    maxNumPreChildren=row["maxNumPreChildren"],
                    maxNumSAgeChildren=row["maxNumSAgeChildren"],
                    LangOfService=row["LangOfService"],
                    operatorId=row["operatorId"],
                    designatedFacility=row["designatedFacility"],
                    
                )
                print("Loaded Original Table. Tanek Stuttgraham 041012512")
                self.record_list.append(facility)
            
            return self.record_list  # Make sure this return is inside the try block

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
            return []  # Return an empty list if there's a database error
        
    def load_all_changed_facilities(self):
        """Method loads All records from changed facility table and converts them to facilityClass instances."""
        try:
            self.cursor.execute("SELECT * FROM changed_childcare_facilities")
            rows = self.cursor.fetchall()  # Fetch all rows as dictionaries
            # Convert each dictionary into a facilityClass instance
            self.record_list = []
            for row in rows:
                facility = facilityClass(
                    facilityId=row["id"],
                    region=row["region"],
                    district=row["district"],
                    licenceNum=row["licenceNum"],
                    facilityName=row["facilityName"],
                    facilityType=row["facilityType"],
                    facilityAddress1=row["facilityAddress1"],
                    facilityAddress2=row["facilityAddress2"],
                    facilityAddress3=row["facilityAddress3"],
                    maxNumofChildren=row["maxNumofChildren"],
                    maxNumInfants=row["maxNumInfants"],
                    maxNumPreChildren=row["maxNumPreChildren"],
                    maxNumSAgeChildren=row["maxNumSAgeChildren"],
                    LangOfService=row["LangOfService"],
                    operatorId=row["operatorId"],
                    designatedFacility=row["designatedFacility"],
                    
                )
                print("Loaded Changed Tabel. Tanek Stuttgraham 041012512")
                self.record_list.append(facility)
            
            return self.record_list  # Make sure this return is inside the try block

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
            return []  # Return an empty list if there's a database error

        
    def load_changed_facility_by_id(self, facilityId):
        """Loads A specified changed facility record by its Id"""
        try:
            prepared_sql = f"SELECT * FROM changed_childcare_facilities WHERE id = %(facilityId)s"
            self.cursor.execute(prepared_sql, {"facilityId":facilityId})
            return self.cursor.fetchone()
        except mysql.connector.Error as e:
            print(f"DataBaseError: {e}")
            return None #Return Nothing If Error occurs
        
    def get_first_available_facility(self):
        """Fetches the first available facility record from the original_childcare_facilities table and creates a facilityClass object."""
        
        try:
            self.cursor.execute("SELECT * FROM original_childcare_facilities ORDER BY id ASC LIMIT 1")
            row = self.cursor.fetchone()  # Fetch the first record
            
            if row:  # If a record exists
                facility = facilityClass(
                    facilityId=row["id"],
                    region=row["region"],
                    district=row["district"],
                    licenceNum=row["licenceNum"],
                    facilityName=row["facilityName"],
                    facilityType=row["facilityType"],
                    facilityAddress1=row["facilityAddress1"],
                    facilityAddress2=row["facilityAddress2"],
                    facilityAddress3=row["facilityAddress3"],
                    maxNumofChildren=row["maxNumofChildren"],
                    maxNumInfants=row["maxNumInfants"],
                    maxNumPreChildren=row["maxNumPreChildren"],
                    maxNumSAgeChildren=row["maxNumSAgeChildren"],
                    LangOfService=row["LangOfService"],
                    operatorId=row["operatorId"],
                    designatedFacility=row["designatedFacility"],
                )
                print("Loading one cuz Tanek Stuttgraham 041012512")
                self.record_list = [facility]  # Store the facility in record_list
                return facility
                
            else:
                print("No facility records found in the database.")
                return None
        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
            return None
        
    def add_to_changed_facilities(self, facility):
        """Adds a facility record to Changed childcare facility table."""
         #Prepared Statement
        prepared_sql = """
        INSERT INTO changed_childcare_facilities (
                    region, district, licenceNum, facilityName, facilityType,
                    facilityAddress1, facilityAddress2, facilityAddress3,
                    maxNumofChildren, maxNumInfants, maxNumPreChildren,
                    maxNumSAgeChildren, LangOfService, operatorId, designatedFacility )
            VALUES (%(region)s, %(district)s, %(licenceNum)s, %(facilityName)s, %(facilityType)s,
                                %(facilityAddress1)s, %(facilityAddress2)s, %(facilityAddress3)s, %(maxNumofChildren)s, %(maxNumInfants)s, %(maxNumPreChildren)s,
                                %(maxNumSAgeChildren)s, %(LangOfService)s, %(operatorId)s, %(designatedFacility)s) """
        
        # Values to insert into the database
        values = {
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
        
        self.cursor.execute(prepared_sql, values)
        self.conn.commit()
        
        self.cursor.execute(" SELECT LAST_INSERT_ID()")
        fetchedId = self.cursor.fetchone()
        
        facility.facilityId = fetchedId['LAST_INSERT_ID()']
        
        self.record_list.append(facility)
        print("Facility Added to Changed Facilty Table Successfully.Tanek Stuttgraham 041012512")
        

    def save_facilities(self):
        """Deletes content in changed facility table and saves new record list as records."""
        try:
            # Delete all existing records
            delete_sql = "DELETE FROM changed_childcare_facilities"
            self.cursor.execute(delete_sql)
            
            # SQL statement for inserting new records
            insert_sql = """
            INSERT INTO changed_childcare_facilities (
                region, district, licenceNum, facilityName, facilityType,
                facilityAddress1, facilityAddress2, facilityAddress3,
                maxNumofChildren, maxNumInfants, maxNumPreChildren,
                maxNumSAgeChildren, LangOfService, operatorId, designatedFacility
            ) VALUES (
                %(region)s, %(district)s, %(licenceNum)s, %(facilityName)s, %(facilityType)s,
                %(facilityAddress1)s, %(facilityAddress2)s, %(facilityAddress3)s, 
                %(maxNumofChildren)s, %(maxNumInfants)s, %(maxNumPreChildren)s,
                %(maxNumSAgeChildren)s, %(LangOfService)s, %(operatorId)s, %(designatedFacility)s
            )"""
            
            # Insert each record from self.record_list
            for record in self.record_list:
                values = {
                    "region": record.region,
                    "district": record.district,
                    "licenceNum": record.licenceNum,
                    "facilityName": record.facilityName,
                    "facilityType": record.facilityType,
                    "facilityAddress1": record.facilityAddress1,
                    "facilityAddress2": record.facilityAddress2,
                    "facilityAddress3": record.facilityAddress3,
                    "maxNumofChildren": record.maxNumofChildren,
                    "maxNumInfants": record.maxNumInfants,
                    "maxNumPreChildren": record.maxNumPreChildren,
                    "maxNumSAgeChildren": record.maxNumSAgeChildren,
                    "LangOfService": record.LangOfService,
                    "operatorId": record.operatorId,
                    "designatedFacility": record.designatedFacility
                }
                self.cursor.execute(insert_sql, values)
            
            # Commit transaction after inserting all records
            self.conn.commit()
            print("All Facilities Saved Successfully. Tanek Stuttgraham 041012512")

        except mysql.connector.Error as e:
            print(f"Database error: {e}")
            self.conn.rollback()  # Rollback changes in case of an error
                
    def update_in_changed_facilities(self, facilityId, updatedValues):
        """Updates an existing Facility in Changed Facilites table."""
        if not updatedValues:
            print("No Updated Values Provided.")
            return
        try:
            prepared_sql = f"UPDATE changed_childcare_facilities SET 	{', '.join(f'{k} = %s' for k in updatedValues.keys())} WHERE id = %s"
            print("Executing SQL:", prepared_sql)
            print("With values:", (*updatedValues.values(), facilityId))

            self.cursor.execute(prepared_sql, (*updatedValues.values(), facilityId))
            
            self.conn.commit()
            print("Updated Succesfully. Tanek Stuttgraham 041012512")
        except mysql.connector.Error as e:
            print("Sql Error : {e} ")
            
                        

    def delete_facility(self, facilityId):
            """Delete a facility from changed_childcare_facilities."""
            try:
                prepared_sql = "DELETE FROM changed_childcare_facilities WHERE id = %(facilityId)s"
                self.cursor.execute(prepared_sql, {"facilityId": facilityId})
                self.conn.commit()
                
                checking_sql = "SELECT * FROM changed_childcare_facilities WHERE id = %(facilityId)s"
                self.cursor.execute(checking_sql , {"facilityId": facilityId})
                delete_result = self.cursor.fetchone()
                
                if delete_result is None:
                    print("Facility deleted successfully.")
                    
                    # Remove from record_list
                    self.record_list = [facility for facility in self.record_list if facility.facilityId != facilityId]
                    print(f"Facility with ID {facilityId} removed from record_list. Tanek Stuttgraham 041012512")
                else:
                    print("Facility deletion failed")
            except mysql.connector.Error as e:
                print(f"Database Error: {e}")
     
            
    def restore_original_facilities(self):
            """Rewrite changed_childcare_facilities with original_childcare_facilities data."""
            self.load_original_to_changed()
            print("Restored changed_childcare_facilities to original state.")
        
    
    def close_connection(self):
        """Close the database connection."""
        self.cursor.close()
        self.conn.close()
    
