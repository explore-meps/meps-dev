import os

from os.path import expanduser
from zipfile import ZipFile

from meps_db.utilities.universal_utilities import UniversalUtilityFunctions as util

from meps_db.components.reference import (
    FYCDF_PUF_LOOKUP,
    FYPCDF_PUF_LOOKUP,
    MCDF_PUF_LOOKUP,
    PMDF_PUF_LOOKUP,
    DVDF_PUF_LOOKUP,
    OMEDF_PUF_LOOKUP,
    HISDF_PUF_LOOKUP,
    ERVDF_PUF_LOOKUP,
    OVDF_PUF_LOOKUP,
    OBMPVDF_PUF_LOOKUP,
    HHDF_PUF_LOOKUP,
)


class BaseComponentsPopulator:
    """ Base class for associated populator classes. Contains common elements that can be used by inheriting classes
    """
    
    @staticmethod
    def get_meps_folder_dir(folder):
        """ Takes a folder name, returns the base meps data folder directory """
        return os.path.join(expanduser("~"), "meps", "meps_data", folder)

    @classmethod
    def get_zip_path(cls, folder, year, year_lookup):
        """ Takes a folder name, a year, and the year lookup dictionary. Returns the full path to the zipped dat file
        """
        return os.path.join(cls.get_meps_folder_dir(folder),f"{year_lookup[year]}dat.zip")
    
    @classmethod
    def get_txt_path(cls, folder, year, year_lookup):
        """ Takes a folder name, a year, and the year lookup dictionary. Returns the full path to the sas txt file
        """
        return os.path.join(cls.get_meps_folder_dir(folder),f"{year_lookup[year]}su.txt")

    @classmethod
    def get_variable_parameters_path(cls, folder, year, year_lookup):
        """ Takes a folder name, a year, and the year lookup dictionary. Returns the full path to the variable 
        parameters json """
        return os.path.join(cls.get_meps_folder_dir(folder),f"{year_lookup[year]}_parameters.json")

    @staticmethod
    def parse_ascii(ascii_text, sas_text):
        """ Takes an ascii text string and sas statement text. Identifies where input statements begin and end in the
        sas text. Builds a dictionary for each variable that identifies where it will be placed in the ascii text. Uses
        that lookup to parse the ascii text and convert it to a list of dictionaries, each associated with a respondent
        """

        std_sas_text = sas_text.split("\n")
        input_index = std_sas_text.index("* INPUT STATEMENTS;")
        format_index = std_sas_text.index("* FORMAT STATEMENTS;")

        # Build map for extracting ascii text
        variable_location_lookup = []
        for row in std_sas_text[input_index:format_index]:
            # skip headers
            if "@" not in row:
                continue
            split_row = row.strip("INPUT").split()
            variable_location_lookup.append(
                {
                    "name": split_row[1],
                    "start": int(float(split_row[0].strip("@"))),
                    "size": int(float(split_row[2].strip("$")))
                }
            )
        
        # extract ascii text
        respondents_dict = []
        row_data = ascii_text.decode("utf-8").split("\r\n")
        for row in row_data[:-1]: # last row is always empty
            respondent_dict = {}
            for var_dict in variable_location_lookup:
                # SAS starts lists on 1, python on 0
                val = row[var_dict["start"]-1:var_dict["start"]-1+var_dict["size"]].strip()
                respondent_dict.update({var_dict["name"]: val})
            
            respondents_dict.append(respondent_dict)
        
        return respondents_dict

    @staticmethod
    def get_variable_parameters(sas_text, respondents_dict):
        """ Takes a string of sas statement text and the list of respondent dictionaries. Creates a list of
        dictionaries for each variable that contains the name, the min and max length and the description. Intended
        to be used for building model classes. """

        std_sas_text = sas_text.split("\n")
        label_index = std_sas_text.index("* LABEL STATEMENTS;")
        value_index = std_sas_text.index("* VALUE STATEMENTS;")

        # get descriptions
        variable_parameters = {}
        for row in std_sas_text[label_index:value_index]:
            if "=" not in row:
                continue
            split_row = row.strip("LABEL").split("=")
            variable_parameters[split_row[0].strip()] = {"description": split_row[1].replace("'", "")}
        
        for var, var_dict in variable_parameters.items():
            values = [len(resp[var]) for resp in respondents_dict]
            var_dict.update({"min": min(values), "max": max(values)})
        
        return variable_parameters

    @classmethod
    def unpack_data(cls, folder, year, year_lookup):
        """ Takes a folder, year and year to PUF no lookup. Unzips the ascii file and uses the txt file to identify
        how variables are placed with respect to each other. Unpacks the ascii file as a list of dictionaries, each
        corresponding to a respondent. Returns list of dictionaries.
        """

        zip_path = cls.get_zip_path(folder=folder, year=year, year_lookup=year_lookup)
        txt_path = cls.get_txt_path(folder=folder, year=year, year_lookup=year_lookup)

        zipped_filename = zip_path.split("/")[-1]
        unzip_path = zip_path.replace(zipped_filename, "")

        with ZipFile(zip_path,"r") as zip_ref:
            zip_ref.extractall(unzip_path)
        
        unzipped_filename = zipped_filename.split("dat.zip")[0]

        # load ascii data, files unpack in somewhat arbitrary format
        ascii_text = None
        for potential_path in [
            os.path.join(unzip_path, f"{unzipped_filename}.dat"),
            os.path.join(unzip_path, f"{unzipped_filename.upper()}.DAT"),
            os.path.join(unzip_path, f"{unzipped_filename.upper()}.dat")
        ]:
            if os.path.exists(potential_path):
                with open(potential_path, 'rb') as f:
                    ascii_text = f.read()
        
        if not ascii_text:
            raise ValueError("No .dat file associated with {unzipped_filename}")

        # load SAS data
        with open(txt_path, 'r') as f:
            sas_text = f.read()
        
        respondents_dict = cls.parse_ascii(ascii_text=ascii_text, sas_text=sas_text)
        variable_parameters = cls.get_variable_parameters(sas_text=sas_text, respondents_dict=respondents_dict)

        return respondents_dict, variable_parameters


class ComponentPopulator(BaseComponentsPopulator):
    """ General populator class, extracts the raw ssp data and converts into dictionaries that can be passed to the 
    the associated model model. """

    def __init__(self, year, data_type):
        """
        Required Input:
            year: year to extract data
            data_type: description of the data requested
        """
        self.year = year
        self.data_type = data_type

        self.data_map = {
            "consolidated": FYCDF_PUF_LOOKUP,
            "population_characteristics": FYPCDF_PUF_LOOKUP,
            "medical_conditions": MCDF_PUF_LOOKUP,
            "prescribed_medicines": PMDF_PUF_LOOKUP,
            "dental_visits": DVDF_PUF_LOOKUP,
            "other_medical_expenses": OMEDF_PUF_LOOKUP,
            "hospital_inpatient_stays": HISDF_PUF_LOOKUP,
            "emergency_room_visits": ERVDF_PUF_LOOKUP,
            "outpatient_visits": OVDF_PUF_LOOKUP,
            "office_based_visits": OBMPVDF_PUF_LOOKUP,
            "home_health": HHDF_PUF_LOOKUP,
        }

        assert self.data_type in self.data_map
    
    def run(self):
        """ Primary Entry point of FYCDFPopulator """

        respondents_dict, variable_parameters = self.unpack_data(
            folder=self.data_type, 
            year=self.year, 
            year_lookup=self.data_map[self.data_type]
        )

        # handle edge where the 2011 FYCDF contains more than 2000 columns, remove fields related to the CSAQ survey
        if self.data_type == "consolidated" and self.year == 2011:
            # fields to pop
            fields_to_pop = []
            for var, var_dict in variable_parameters.items():
                if "CSAQ:" in var_dict["description"]:
                    fields_to_pop.append(var)

            for resp_dict in respondents_dict:
                for field in fields_to_pop:
                    resp_dict.pop(field)

        variable_parameters_path = os.path.join(
            self.get_meps_folder_dir(folder=self.data_type), f"{self.data_map[self.data_type][self.year]}_parameters"
        )
        util.write_data_to_file(
            data=variable_parameters,
            output_file_path=variable_parameters_path,
            output_file_format="json"
        )

        return respondents_dict
