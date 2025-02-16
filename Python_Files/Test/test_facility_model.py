import unittest
import sys
import os
import csv

# Ensure Python_Files is in the module search path 
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
    
from Model.facilityClass import facilityClass
from Model.facilityModel import FacilityModel

class TestFacilityModel(unittest.TestCase):
    
    def setUp(self):
        """Set up testing environment before test is ran"""
        self.model = FacilityModel() #FacilityModel instance
        self.model.load_from_csv()  # Load all records from CSV
        self.test_facility = self.model.load_one_from_csv(0)
        
    def test_loading(self):
        """Tests to see if csv is loaded into memory. If number loaded is greater than zero."""
        self.assertGreater(len(self.model.record_list), 0, "No Records Loaded")
        
    def test_each_variable(self):
        """Tests each variable of a facility to see if they are properly loaded. assertIsInstance checks for an object variable"""
        # Load the facility
        self.test_facility = self.model.load_one_from_csv(0)
        self.assertIsInstance(self.test_facility.facilityName, str, "No FacilityName")
        print(f"AAAAAAAAAAAAAAAAAFacility Name: {self.test_facility.facilityName}")
        self.assertIsInstance(self.test_facility.facilityType, str)
        self.assertIsInstance(self.test_facility.region, str)
        self.assertIsInstance(self.test_facility.district, str)
        self.assertIsInstance(self.test_facility.licenseNum, str)
        self.assertIsInstance(self.test_facility.maxNumofChildren, int) #Only testing max number of children
        self.assertIsInstance(self.test_facility.LangOfService, str)
        self.assertIsInstance(self.test_facility.operatorId, str)
        self.assertIsInstance(self.test_facility.designatedFacility, str)
        
        
    def test_save_facilities(self):
        """Tests the saving of facilities to a CSV"""
        saving_file_path = "C:/AAFINAL-SEMESTER/Programming Language Research Project/Practical_Project/Saved_Facility_CSV.csv"
        self.model.save_facilities()  # Save the facilities data
        
        # Verify if the file was created
        self.assertTrue(os.path.exists(saving_file_path), "Saved file does not exist")
        
        # Optionally, you can read the saved file and verify its contents:
        with open(saving_file_path, mode='r') as file:
            csvFile = csv.reader(file)
            header = next(csvFile)
            self.assertIn('Region', header, "Header 'Region' not found in saved CSV")
        
    
    def tearDown(self):
        """Cleanup method """
        self.model = None

        
if __name__ == "__main__":
    unittest.main()
        
