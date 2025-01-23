class FacilityClass:
    # Constructor for the records in the CSV
    def __init__(self, region, district, licenseNum, facilityName, facilityType, facilityAddress1,
                 facilityAddress2, facilityAddress3, maxNumofChildren, maxNumInfants, maxNumPreChildren,
                 maxNumSAgeChildren, LangOfService, operatorId, designatedFacility):
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

    # Getter and Setter for region
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        self._region = value

    # Getter and Setter for district
    @property
    def district(self):
        return self._district

    @district.setter
    def district(self, value):
        self._district = value

    # Getter and Setter for licenseNum
    @property
    def licenseNum(self):
        return self._licenseNum

    @licenseNum.setter
    def licenseNum(self, value):
        self._licenseNum = value

    # Getter and Setter for facilityName
    @property
    def facilityName(self):
        return self._facilityName

    @facilityName.setter
    def facilityName(self, value):
        self._facilityName = value

    # Getter and Setter for facilityType
    @property
    def facilityType(self):
        return self._facilityType

    @facilityType.setter
    def facilityType(self, value):
        self._facilityType = value

    # Getter and Setter for facilityAddress1
    @property
    def facilityAddress1(self):
        return self._facilityAddress1

    @facilityAddress1.setter
    def facilityAddress1(self, value):
        self._facilityAddress1 = value

    # Getter and Setter for facilityAddress2
    @property
    def facilityAddress2(self):
        return self._facilityAddress2

    @facilityAddress2.setter
    def facilityAddress2(self, value):
        self._facilityAddress2 = value

    # Getter and Setter for facilityAddress3
    @property
    def facilityAddress3(self):
        return self._facilityAddress3

    @facilityAddress3.setter
    def facilityAddress3(self, value):
        self._facilityAddress3 = value

    # Getter and Setter for maxNumofChildren
    @property
    def maxNumofChildren(self):
        return self._maxNumofChildren

    @maxNumofChildren.setter
    def maxNumofChildren(self, value):
        self._maxNumofChildren = value

    # Getter and Setter for maxNumInfants
    @property
    def maxNumInfants(self):
        return self._maxNumInfants

    @maxNumInfants.setter
    def maxNumInfants(self, value):
        self._maxNumInfants = value

    # Getter and Setter for maxNumPreChildren
    @property
    def maxNumPreChildren(self):
        return self._maxNumPreChildren

    @maxNumPreChildren.setter
    def maxNumPreChildren(self, value):
        self._maxNumPreChildren = value

    # Getter and Setter for maxNumSAgeChildren
    @property
    def maxNumSAgeChildren(self):
        return self._maxNumSAgeChildren

    @maxNumSAgeChildren.setter
    def maxNumSAgeChildren(self, value):
        self._maxNumSAgeChildren = value

    # Getter and Setter for LangOfService
    @property
    def LangOfService(self):
        return self._LangOfService

    @LangOfService.setter
    def LangOfService(self, value):
        self._LangOfService = value

    # Getter and Setter for operatorId
    @property
    def operatorId(self):
        return self._operatorId

    @operatorId.setter
    def operatorId(self, value):
        self._operatorId = value

    # Getter and Setter for designatedFacility
    @property
    def designatedFacility(self):
        return self._designatedFacility

    @designatedFacility.setter
    def designatedFacility(self, value):
        self._designatedFacility = value
