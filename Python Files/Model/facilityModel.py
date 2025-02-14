import csv
from Model.facilityClass import facilityClass
"""This file (FacilityModel) was written by Tanek Stuttgraham Student No 041012512, Course Code: CST8002_050, Prof. Todd Keuleman"""

# File path to the CSV
file_path = r"C:\AAFINAL-SEMESTER\Programming Language Research Project\Practical_Project\Licensed_Early_Learning_and_Childcare_Facilities.csv"
saving_file_path = "C:/AAFINAL-SEMESTER/Programming Language Research Project/Practical_Project/Saved_Facility_CSV.csv"

class FacilityModel:
    def __init__(self):
        """Initialize FacilityModel with empty record list."""
        self.record_list = []  # List to store facility objects

    def load_from_csv(self):
        """Load facility data from the CSV and populate the record list."""
        try:
            with open(file_path, mode='r') as file:
                # Each row becomes a dictionary, csv.DictReader pairs keys and data
                csvFile = csv.DictReader(file)
                # Loop through each row, limited to 100 records
                for i, lines in enumerate(csvFile, start=1):
                    if i <= 100:  # Read only 100 records
                        print(f"Records Read According To Tanek Stuttgraham 041012512 --> {i}")
                        try:   # Create a facilityClass object and pass each row value into the correct variable.
                            facility = facilityClass(
                                region=lines['Region'],
                                district=lines['District'],
                                licenseNum=lines['License-Number'],
                                facilityName=lines['Facility-Name'],
                                facilityType=lines['Facility-Type'],
                                facilityAddress1=lines['Facility-Address-1'],
                                facilityAddress2=lines['Facility-Address-2'],
                                facilityAddress3=lines['Facility-Address-3'],
                                maxNumofChildren=int(lines['Max-Number-of-Children']),
                                maxNumInfants=int(lines['Max-Number-of-Infants']),
                                maxNumPreChildren=int(lines['Max-Number-of-Preschool-Aged-Children']),
                                maxNumSAgeChildren=int(lines['Max-Number-of-School-Age-Children']),
                                LangOfService=lines['Language-of-Service'],
                                operatorId=lines['Operator-Id'],
                                designatedFacility=lines['Designated-Facility']
                            )
                            # Append record object to the list
                            self.record_list.append(facility)

                        except KeyError as e:
                            print(f"Key Error, Missing column or value: {e}")
                        except ValueError as e:
                            print(f"Data Type Error, Wrong Value Passed: {e}")

                        if i % 10 == 0:
                            print("Program By Tanek Stuttgraham 041012512")

            print(f"According to Tanek Stuttgraham we've read {len(self.record_list)} records.")
            print("Facility Records:")
            # Print all records in the list
            for i, facility in enumerate(self.record_list, start=1):
                print(facility)
                print(i)

        except IOError as e:
            print(f"IO Error, Make sure the file path is correct: {e}")

    def save_facilities(self):
        """Save the facilities data to a CSV file."""
        try:
            with open(saving_file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                # Writing Headers
                writer.writerow(['Region', 'District', 'License-Number', 'Facility-Name',
                                 'Facility-Type', 'Facility-Address-1', 'Facility-Address-2',
                                 'Facility-Address-3', 'Max-Number-of-Children',
                                 'Max-Number-of-Infants', 'Max-Number-of-Preschool-Aged-Children',
                                 'Max-Number-of-School-Age-Children', 'Language-of-Service',
                                 'Operator-Id', 'Designated-Facility'])

                # Write Facility Object Data
                for facility in self.record_list:
                    writer.writerow([facility.region, facility.district, facility.licenseNum,
                                     facility.facilityName, facility.facilityType,
                                     facility.facilityAddress1, facility.facilityAddress2,
                                     facility.facilityAddress3, facility.maxNumofChildren,
                                     facility.maxNumInfants, facility.maxNumPreChildren,
                                     facility.maxNumSAgeChildren, facility.LangOfService,
                                     facility.operatorId, facility.designatedFacility])

            print(f"Successfully saved data to {saving_file_path}")

        except IOError as e:
            print(f"IO Error, Did not save: {e}")
