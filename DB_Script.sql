use pythondb;
select *  FROM changed_childcare_facilities;
Select * from original_childcare_facilities;
SELECT * FROM changed_childcare_facilities;
INSERT INTO changed_childcare_facilities SELECT * FROM original_childcare_facilities;
CREATE TABLE original_childcare_facilities (
    id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each record
    region VARCHAR(255),                     -- Region where the facility is located
    district VARCHAR(255),                   -- District where the facility is located
    licenceNum VARCHAR(255),                 -- Licence number of the facility
    facilityName VARCHAR(255),               -- Facility's name
    facilityType VARCHAR(255),               -- Type of facility
    facilityAddress1 VARCHAR(255),           -- Primary address of the facility
    facilityAddress2 VARCHAR(255),           -- Secondary address of the facility
    facilityAddress3 VARCHAR(255),           -- Tertiary address of the facility
    maxNumofChildren INT,                    -- Maximum number of children the facility can contain
    maxNumInfants INT,                       -- Maximum number of infants the facility can contain
    maxNumPreChildren INT,                   -- Maximum number of preschool-age children the facility can contain
    maxNumSAgeChildren INT,                  -- Maximum number of school-age children the facility can contain
    LangOfService VARCHAR(255),              -- Primary language spoken at the facility
    operatorId VARCHAR(255),                 -- Operator ID for the facility
    designatedFacility INT                   -- Number of designated facilities
);

CREATE TABLE changed_childcare_facilities (
    id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each record
    region VARCHAR(255),                     -- Region where the facility is located
    district VARCHAR(255),                   -- District where the facility is located
    licenceNum VARCHAR(255),                 -- Licence number of the facility
    facilityName VARCHAR(255),               -- Facility's name
    facilityType VARCHAR(255),               -- Type of facility
    facilityAddress1 VARCHAR(255),           -- Primary address of the facility
    facilityAddress2 VARCHAR(255),           -- Secondary address of the facility
    facilityAddress3 VARCHAR(255),           -- Tertiary address of the facility
    maxNumofChildren INT,                    -- Maximum number of children the facility can contain
    maxNumInfants INT,                       -- Maximum number of infants the facility can contain
    maxNumPreChildren INT,                   -- Maximum number of preschool-age children the facility can contain
    maxNumSAgeChildren INT,                  -- Maximum number of school-age children the facility can contain
    LangOfService VARCHAR(255),              -- Primary language spoken at the facility
    operatorId VARCHAR(255),                 -- Operator ID for the facility
    designatedFacility INT                   -- Number of designated facilities
);
