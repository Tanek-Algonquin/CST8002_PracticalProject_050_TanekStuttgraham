import mysql.connector
import csv
"""This is a helper class inteded to refresh the original_childcare_facilities table in the database.
      It reads from a csv and inserts per records to the database."""
def connect_to_databse():
    """Connect to My SQL workbench DB, return a connection"""
    conn = mysql.connector.connect (
        host="localhost",
        user="cst8277",
        password="8277",
        database="pythondb"
        )
    return conn

file_path = r"C:\AAFINAL-SEMESTER\Programming Language Research Project\Practical_Project\Licensed_Early_Learning_and_Childcare_Facilities.csv"

def load_csv_to_db(file_path):
    """Load From Csv To Database."""
    try:
        #Initialize Connection and Cursor
        connection = connect_to_databse()
        cursor = connection.cursor()
        
        #Open CSV File
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            
            #Read Records in CSV
            for i, row in enumerate(reader, start=1):
                try:
                    region=row['Region']
                    district=row['District']
                    licenceNum=row['License-Number'] 
                    facilityName=row['Facility-Name']
                    facilityType=row['Facility-Type']
                    facilityAddress1=row['Facility-Address-1']
                    facilityAddress2=row['Facility-Address-2']
                    facilityAddress3=row['Facility-Address-3']
                    maxNumofChildren=int(row['Max-Number-of-Children']) if row['Max-Number-of-Children'] else 0
                    maxNumInfants=int(row['Max-Number-of-Infants']) if row['Max-Number-of-Infants'] else 0
                    maxNumPreChildren=int(row['Max-Number-of-Preschool-Aged-Children']) if row['Max-Number-of-Preschool-Aged-Children'] else 0
                    maxNumSAgeChildren=int(row['Max-Number-of-School-Age-Children']) if row['Max-Number-of-School-Age-Children'] else 0
                    LangOfService=row['Language-of-Service']
                    operatorId=row['Operator-Id']
                    designatedFacility=row['Designated-Facility']
                    
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
                    
                    #Cursor Executing Statement
                    cursor.execute(prepared_sql, values)
                    
                    #Commit Transaction
                    connection.commit()
                
                except Exception as e:
                    print(f"Error inserting row {i}: {e}")

    except Exception as e:
        print(f"Error connecting to the database: {e}")
    
    finally:
        # Close the connection and cursor
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Call the function to load the CSV into the DB
load_csv_to_db(file_path)