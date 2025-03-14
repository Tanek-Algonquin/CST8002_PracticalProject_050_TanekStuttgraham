class facilityClass:
    """
This file (facilityClass) was written by Tanek Stuttgraham Student No 041012512, Course Code: CST8002_050, Prof. Todd Keuleman
 This class represents a liscenced childcare facility found in the csv dataset provided.
  Attributes:
 -region (str) : The region where this facility is located.
 -district (str) : The district where this facility is located.
 -liscenceNum (str): The liscence number of this facility.
 -facilityName (str) : This facilities name.
 -facilityType (str) : This facilities type.
 -facilityAddress1 (str) : The primary address of this facility.
-facilityAddress2 (str) : The secondary address of this facility.
-facilityAddress3 (str) : The tertiary address of this facility.
-maxNumofChildren (int) : The maximum ammount of children this facilty can contain.
-maxNumInfants (int) : The maximum ammount of infants this facilty can contain.
-maxNumPreChildren (int) : The maximum ammount of pre-school age children this facilty can contain.
-maxNumSAgeChildren (int) : The maximum ammount of school children this facilty can contain.
-LangOfService (str) : The primary language spoken at this facility.
-operatorId (str) : The operator Id of this facility
-designatedFacility (str) : The ammount of designated facilities for this facility.
"""
    # Constructor for the records in the CSV
    def __init__(self, facilityId, region, district, licenseNum, facilityName, facilityType, facilityAddress1,
                 facilityAddress2, facilityAddress3, maxNumofChildren, maxNumInfants, maxNumPreChildren,
                 maxNumSAgeChildren, LangOfService, operatorId, designatedFacility):
        """
    Initialized facility object with parametres passed from csv record.
    Parameters:
-facilityId (int) : Id for facility in DB
-region (str) : The region where this facility is located.
-district (str) : The district where this facility is located.
-liscenceNum (str): The liscence number of this facility.
-facilityName (str) : This facilities name.
-facilityType (str) : This facilities type.
-facilityAddress1 (str) : The primary address of this facility.
-facilityAddress2 (str) : The secondary address of this facility.
-facilityAddress3 (str) : The tertiary address of this facility.
-maxNumofChildren (int) : The maximum ammount of children this facilty can contain.
-maxNumInfants (int) : The maximum ammount of infants this facilty can contain.
-maxNumPreChildren (int) : The maximum ammount of pre-school age children this facilty can contain.
-maxNumSAgeChildren (int) : The maximum ammount of school children this facilty can contain.
-LangOfService (str) : The primary language spoken at this facility.
-operatorId (str) : The operator Id of this facility
-designatedFacility (str) : The ammount of designated facilities for this facility.
"""
        self.facilityId = facilityId
        self._region = region
        self._district = district
        self._licenseNum = licenseNum
        self._facilityName = facilityName
        self._facilityType = facilityType
        self._facilityAddress1 = facilityAddress1
        self._facilityAddress2 = facilityAddress2
        self._facilityAddress3 = facilityAddress3
        self._maxNumofChildren = maxNumofChildren
        self._maxNumInfants = maxNumInfants
        self._maxNumPreChildren = maxNumPreChildren
        self._maxNumSAgeChildren = maxNumSAgeChildren
        self._LangOfService = LangOfService
        self._operatorId = operatorId
        self._designatedFacility = designatedFacility
     
     # __str__ helps customize output. Bold text I realize that the shell does not display Boldened letters
    def  __str__(self):
        """
A custom string representation of the facilities data.
"""
        return (
            f"Tanek Stuttgraham approves of this facility ;\n"
            f"facilityId : {self.facilityId} , \n"
            f"Region : {self._region},  \n"
            f"District : {self._district}, \n"
            f"License number : {self._licenseNum}, \n"
            f"Facility name: {self._facilityName}, \n"
            f"Facility type : {self._facilityType}, \n"
            f"First facilityAddress : {self._facilityAddress1}, \n"
            f"Second facility address : {self._facilityAddress2}, \n"
            f"Third facility address : {self._facilityAddress3}, \n"
            f"Maximum number of children : {self._maxNumofChildren}, \n"
            f"Maximum number of infants : {self._maxNumInfants}, \n"
            f"Maximum number of pre-school aged children : {self._maxNumPreChildren}, \n"
            f"Maximum number of school aged children : {self._maxNumSAgeChildren}, \n"
            f"Language of service : {self._LangOfService}, \n"
            f"Operator Id : {self._operatorId}, \n"
            f"Designated facility : {self._designatedFacility}" )

    """Getter for region"""
    @property
    def region(self):
        return self._region
    """Setter for region"""
    @region.setter
    def region(self, value):
        self._region = value
    
    """Getter For Facility Id"""   
    @property
    def facilityId(self):
        return self._facilityId
    """Setter For Facility Id"""
    @facilityId.setter
    def facilityId(self, value):
        self._facilityId = value
    """Getter for district"""
    @property
    def district(self):
        return self._district
    """Setter for district"""
    @district.setter
    def district(self, value):
        self._district = value

    """Getter for licenseNum"""
    @property
    def licenseNum(self):
        return self._licenseNum
    """Setter for licenseNum"""
    @licenseNum.setter
    def licenseNum(self, value):
        self._licenseNum = value

    """Setter for facilityName"""
    @property
    def facilityName(self):
        return self._facilityName
    """Setter for facilityName"""
    @facilityName.setter
    def facilityName(self, value):
        self._facilityName = value

    """Getter for facilityType"""
    @property
    def facilityType(self):
        return self._facilityType
    """Setter for facilityType"""
    @facilityType.setter
    def facilityType(self, value):
        self._facilityType = value

    """Getter for facilityAddress1"""
    @property
    def facilityAddress1(self):
        return self._facilityAddress1
    """Setter for facilityAddress1"""
    @facilityAddress1.setter
    def facilityAddress1(self, value):
        self._facilityAddress1 = value

    """Getter for facilityAddress2"""
    @property
    def facilityAddress2(self):
        return self._facilityAddress2
    """Setter for facilityAddress2"""
    @facilityAddress2.setter
    def facilityAddress2(self, value):
        self._facilityAddress2 = value

    """Getter for facilityAddress3"""
    @property
    def facilityAddress3(self):
        return self._facilityAddress3
    """Setter for facilityAddress3"""
    @facilityAddress3.setter
    def facilityAddress3(self, value):
        self._facilityAddress3 = value

    """Getter for maxNumofChildren"""
    @property
    def maxNumofChildren(self):
        return self._maxNumofChildren
    """Setter for maxNumofChildren"""
    @maxNumofChildren.setter
    def maxNumofChildren(self, value):
        self._maxNumofChildren = value

    """Getter for maxNumInfants"""
    @property
    def maxNumInfants(self):
        return self._maxNumInfants
    """Setter for maxNumInfants"""
    @maxNumInfants.setter
    def maxNumInfants(self, value):
        self._maxNumInfants = value

    """Getter for maxNumPreChildren"""
    @property
    def maxNumPreChildren(self):
        return self._maxNumPreChildren
    """Setter for maxNumPreChildren"""
    @maxNumPreChildren.setter
    def maxNumPreChildren(self, value):
        self._maxNumPreChildren = value

    """Getter for maxNumSAgeChildren"""
    @property
    def maxNumSAgeChildren(self):
        return self._maxNumSAgeChildren
    """Setter for maxNumSAgeChildren"""
    @maxNumSAgeChildren.setter
    def maxNumSAgeChildren(self, value):
        self._maxNumSAgeChildren = value

    """Getter for LangOfService"""
    @property
    def LangOfService(self):
        return self._LangOfService
    """Setter for LangOfService"""
    @LangOfService.setter
    def LangOfService(self, value):
        self._LangOfService = value

    """Getter for operatorId"""
    @property
    def operatorId(self):
        return self._operatorId
    """Setter for operatorId"""
    @operatorId.setter
    def operatorId(self, value):
        self._operatorId = value

    """Getter for designatedFacility"""
    @property
    def designatedFacility(self):
        return self._designatedFacility
    """Setter for designatedFacility"""
    @designatedFacility.setter
    def designatedFacility(self, value):
        self._designatedFacility = value
