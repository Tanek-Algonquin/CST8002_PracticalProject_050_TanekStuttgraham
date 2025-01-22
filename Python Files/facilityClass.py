class facilityClass:
    # While class variables aren't necessary, I wanted to have all the variables written out.
    region = None
    district = None
    licenseNum = None
    facilityName = None
    facilityType = None
    facilityAddress1 = None
    facilityAddress2 = None
    facilityAddress3 = None
    maxNumofChildren = None
    maxNumInfants = None
    maxNumPreChildren = None
    maxNumSAgeChildren = None
    LangOfService = None
    operatorId = None
    designatedFacility = None

    # Constructor for the records in the CSV
    def __init__(self, region, district, licenseNum, facilityName, facilityType, facilityAddress1,
                 facilityAddress2, facilityAddress3, maxNumofChildren, maxNumInfants, maxNumPreChildren,
                 maxNumSAgeChildren, LangOfService, operatorId, designatedFacility):
        self.region = region
        self.district = district
        self.licenseNum = licenseNum
        self.facilityName = facilityName
        self.facilityType = facilityType
        self.facilityAddress1 = facilityAddress1
        self.facilityAddress2 = facilityAddress2
        self.facilityAddress3 = facilityAddress3
        self.maxNumofChildren = maxNumofChildren
        self.maxNumInfants = maxNumInfants
        self.maxNumPreChildren = maxNumPreChildren
        self.maxNumSAgeChildren = maxNumSAgeChildren
        self.LangOfService = LangOfService
        self.operatorId = operatorId
        self.designatedFacility = designatedFacility
