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
        self.test_facility = self.model.get_first_available_facility()    
    def test_loading(self):
        """Tests to see if database records are loaded into memory. If number loaded is greater than zero."""
        self.assertGreater(len(self.model.record_list), 0, "No Records Loaded")
    def test_each_variable(self):
        """Tests each variable of a facility to see if they are properly loaded. assertIsInstance checks for an object variable"""
        self.assertIsInstance(self.test_facility.facilityName, str, "No FacilityName")
        print(f"AAAAAAAAAAAAAAAAAFacility Name: {self.test_facility.facilityName}")
        self.assertIsInstance(self.test_facility.facilityId, int)
        self.assertIsInstance(self.test_facility.facilityType, str)
        self.assertIsInstance(self.test_facility.region, str)
        self.assertIsInstance(self.test_facility.district, str)
        self.assertIsInstance(self.test_facility.licenceNum, str)
        self.assertIsInstance(self.test_facility.maxNumofChildren, int) #Only testing max number of children
        self.assertIsInstance(self.test_facility.LangOfService, str)
        self.assertIsInstance(self.test_facility.operatorId, str)
        self.assertIsInstance(self.test_facility.designatedFacility, int)
       
    def tearDown(self):
        """Cleanup method """
        self.model = None
if __name__ == "__main__":
    unittest.main()
        
