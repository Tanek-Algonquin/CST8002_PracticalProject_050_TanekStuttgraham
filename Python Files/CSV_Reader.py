import csv
from facilityClass import facilityClass

# List to store facility objects
record_list = []

# File path to the CSV
file_path = r"C:\AAFINAL-SEMESTER\Programming Language Research Project\Practical_Project\Licensed_Early_Learning_and_Childcare_Facilities.csv"

# Read CSV (Mode = Read only)
try:
    with open(file_path, mode='r') as file:
        # Each row becomes a dictionary, csv.DictReader pairs keys and data
        csvFile = csv.DictReader(file)
    
        # Loop through each row, limit to 4 records
        for i, lines in enumerate(csvFile, start=1):
            if i <= 4:  # <= 4 for the first 4 records
                print("Record Number According To Tanek Stuttgraham 041012512:")
                print(i)
                print(lines)
                
                try:   # Create an instance of facilityClass for each row
                    facility = facilityClass(
                        region= lines['Region'],
                        district= lines['District'],
                        licenseNum = lines['License-Number'],
                        facilityName = lines['Facility-Name'],
                        facilityType = lines['Facility-Type'],
                        facilityAddress1 = lines['Facility-Address-1'],
                        facilityAddress2 = lines['Facility-Address-2'],
                        facilityAddress3 = lines['Facility-Address-3'],
                        #int(lines[]) change string to int
                        maxNumofChildren = int(lines['Max-Number-of-Children']),
                        maxNumInfants = int(lines['Max-Number-of-Infants']),
                        maxNumPreChildren = int(lines['Max-Number-of-Preschool-Aged-Children']),
                        maxNumSAgeChildren = int(lines['Max-Number-of-School-Age-Children']),
                        
                        LangOfService = lines['Language-of-Service'],
                        operatorId = lines['Operator-Id'],
                        designatedFacility = lines['Designated-Facility']
                    )

                    # Append record object to the list
                    record_list.append(facility)

                # Handle exceptions for missing keys or invalid data types
                except KeyError as e:
                    print(f"Key Error, Missing column or value: {e}")
                except ValueError as e:
                    print(f"Data Type Error, Wrong Value Passed: {e}")
    print("According to Tanek Stuttgraham there are :")
    print(len(record_list))
    print("Facility Records")
    # Print all records in the list
    for facility in record_list:
        print(facility)
        
        
#Handle if filepath is incorrect
except IOError as e:
    print(f"IO Error, Make sure the file path is correct: {e}")
