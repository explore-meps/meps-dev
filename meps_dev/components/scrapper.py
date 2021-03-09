import os
import shutil
import time

from os.path import expanduser
from selenium import webdriver

from meps_dev.components.reference import (
    DATA_FILES_BASE_URL,
    DATA_FILES_YEARS,
    FYCDF_PUF_SSP_LOOKUP,
    FYPCDF_PUF_SSP_LOOKUP,
    MCDF_PUF_SSP_LOOKUP,
    PMDF_PUF_SSP_LOOKUP,
    DVDF_PUF_SSP_LOOKUP,
    OMEDF_PUF_SSP_LOOKUP,
    HISDF_PUF_SSP_LOOKUP,
    ERVDF_PUF_SSP_LOOKUP,
    OVDF_PUF_SSP_LOOKUP,
    OBMPVDF_PUF_SSP_LOOKUP,
    HHDF_PUF_SSP_LOOKUP,
    FYCDF_PUF_CODEBOOK_LOOKUP,
    FYPCDF_PUF_CODEBOOK_LOOKUP,
    MCDF_PUF_CODEBOOK_LOOKUP,
    PMDF_PUF_CODEBOOK_LOOKUP,
    DVDF_PUF_CODEBOOK_LOOKUP,
    OMEDF_PUF_CODEBOOK_LOOKUP,
    HISDF_PUF_CODEBOOK_LOOKUP,
    ERVDF_PUF_CODEBOOK_LOOKUP,
    OVDF_PUF_CODEBOOK_LOOKUP,
    OBMPVDF_PUF_CODEBOOK_LOOKUP,
    HHDF_PUF_CODEBOOK_LOOKUP,
)
from meps_dev.utilities.universal_utilities import UniversalUtilityFunctions

class ScrapMEPSSSP:
    """ Web scrapper class. Uses Selenium to navigate to the MEPS AHRQ Data files page in browser. Downloads ssp files
    to the specified input file location. Requires a chromedriver associated with the version of chrome running on
    the local machine. Follow instructions on https://chromedriver.chromium.org/downloads to identify the driver suited
    for the local machine. """

    def __init__(self, years=None, download_dir=None, sleep=10):
        """
        Required Inputs:
            None   
        Optional Inputs:
            years: years to fetch data for (list of ints ex: [2019, 2020])
            download_dir: specify location to store outputted data (str)
            sleep: seconds to wait for downloads to complete, increase if any files are stored with CRDOWNLOAD 
                extensions
        """

        self.years = years if years else DATA_FILES_YEARS
        self.download_dir = download_dir if download_dir else os.path.join(expanduser("~"), "meps", "meps_data")
        self.sleep = sleep

    def run(self):
        """ Primary entry point of ScrapMEPS """

        self.get_data_files(folder="consolidated", year_lookup=FYCDF_PUF_SSP_LOOKUP)
        self.get_data_files(folder="population_characteristics", year_lookup=FYPCDF_PUF_SSP_LOOKUP)
        self.get_data_files(folder="medical_conditions", year_lookup=MCDF_PUF_SSP_LOOKUP)
        self.get_data_files(folder="prescribed_medicines", year_lookup=PMDF_PUF_SSP_LOOKUP)

        self.get_data_files(folder="dental_visits", year_lookup=DVDF_PUF_SSP_LOOKUP)
        self.get_data_files(folder="other_medical_expenses", year_lookup=OMEDF_PUF_SSP_LOOKUP)
        self.get_data_files(folder="hospital_inpatient_stays", year_lookup=HISDF_PUF_SSP_LOOKUP)
        self.get_data_files(folder="emergency_room_visits", year_lookup=ERVDF_PUF_SSP_LOOKUP)
        self.get_data_files(folder="outpatient_vists", year_lookup=OVDF_PUF_SSP_LOOKUP)
        self.get_data_files(folder="office_based_medical_provider_visits", year_lookup=OBMPVDF_PUF_SSP_LOOKUP)
        self.get_data_files(folder="home_health", year_lookup=HHDF_PUF_SSP_LOOKUP)

    def get_data_files(self, folder, year_lookup):
        """ Takes a folder name and a year to PUF no. lookup. Sets the download directory to the folder name within the
        output directory. Spools up the chromedriver and downloads all files in the years list """

        download_dir = os.path.join(self.download_dir, folder)
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)
        else:
            shutil.rmtree(download_dir)

        chrome_options = webdriver.ChromeOptions()
        prefs = {"download.default_directory": download_dir}
        chrome_options.add_experimental_option("prefs", prefs)
        executable_path = os.path.join(os.path.join(expanduser("~"), "meps", "meps_dev", "chromedriver"))
        driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)

        for year in self.years:
            driver.get(f"{DATA_FILES_BASE_URL}{year_lookup[year]}")

        time.sleep(self.sleep)
        driver.close()

        self.validate_downloads(download_dir=download_dir, year_lookup=year_lookup, years=self.years)

    @staticmethod
    def validate_downloads(download_dir, year_lookup, years):
        """ Takes a download path, a year to PUF no. lookup and the targeted years. Validates that all expected files
        have been downloaded.
        """

        downloads = os.listdir(download_dir)
        missing_files = [
            expected_file
            for year, expected_file in year_lookup.items()
            if year in years and expected_file not in downloads
        ]

        if len(missing_files) > 0:
            raise AssertionError(
                f"The following files were not able to be fetched {', '.join(missing_files)} check if the PUF "
                f"numbers have been updated"
            )

class ScrapMEPSCodebook:
    """ Web scrapper class. Uses Selenium to navigate to the MEPS AHRQ Data files Codebook page in browser. Extracts
    For each variable in a the code book sotres the variable name, description and format. Requires a chromedriver 
    associated with the version of chrome running on the local machine. Follow instructions on
    https://chromedriver.chromium.org/downloads to identify the driver suited for the local machine. """

    def __init__(self, years=None, output_dir=None, sleep=1):
        """
        Required Inputs:
            None   
        Optional Inputs:
            years: years to fetch data for (list of ints ex: [2019, 2020])
            output_dir: location of outputted codebook data
            sleep: seconds to wait for urls to load before scrapping
        """

        self.years = years if years else DATA_FILES_YEARS
        self.output_dir = output_dir if output_dir else os.path.join(expanduser("~"), "meps", "meps_data")
        self.sleep = sleep
    
    def run(self):
        """ Primary entry point of ScrapMEPS """

        self.get_codebook_data(folder="consolidated", year_lookup=FYCDF_PUF_CODEBOOK_LOOKUP)
        self.get_codebook_data(folder="population_characteristics", year_lookup=FYPCDF_PUF_CODEBOOK_LOOKUP)
        self.get_codebook_data(folder="medical_conditions", year_lookup=MCDF_PUF_CODEBOOK_LOOKUP)
        self.get_codebook_data(folder="prescribed_medicines", year_lookup=PMDF_PUF_CODEBOOK_LOOKUP)

        self.get_codebook_data(folder="dental_visits", year_lookup=DVDF_PUF_CODEBOOK_LOOKUP)
        self.get_codebook_data(folder="other_medical_expenses", year_lookup=OMEDF_PUF_CODEBOOK_LOOKUP)
        self.get_codebook_data(folder="hospital_inpatient_stays", year_lookup=HISDF_PUF_CODEBOOK_LOOKUP)
        self.get_codebook_data(folder="emergency_room_visits", year_lookup=ERVDF_PUF_CODEBOOK_LOOKUP)
        self.get_codebook_data(folder="outpatient_vists", year_lookup=OVDF_PUF_CODEBOOK_LOOKUP)
        self.get_codebook_data(folder="office_based_medical_provider_visits", year_lookup=OBMPVDF_PUF_CODEBOOK_LOOKUP)
        self.get_codebook_data(folder="home_health", year_lookup=HHDF_PUF_CODEBOOK_LOOKUP)

    def get_codebook_data(self, folder, year_lookup):
        """ Takes a folder name and a year to PUF no. lookup. Spools up the chromedriver and extracts all codebook
        data related to variables. Stores in the output directory. """

        output_dir = os.path.join(self.output_dir, folder)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        executable_path = os.path.join(os.path.join(expanduser("~"), "meps", "meps_dev", "chromedriver"))
        driver = webdriver.Chrome(executable_path=executable_path)  

        for year in self.years:
            PUFId = year_lookup[year]
            url = f"https://www.meps.ahrq.gov/mepsweb/data_stats/download_data_files_codebook.jsp?PUFId={PUFId}"
            driver.get(url)
            time.sleep(self.sleep)
            table_css = driver.find_element_by_css_selector(
                "body > table:nth-child(24) > tbody > tr:nth-child(2) > td:nth-child(3) > table:nth-child(5) > tbody >"
                " tr > td > table:nth-child(3)"
            )
            # generate codebook keys
            table_str = table_css.text
            table_text = table_str.split("\n")
            last_header_ind = table_text.index("Description") + 1

            keys = table_text[:last_header_ind]
            vals = table_text[last_header_ind:]

            variables = []
            for field_num in range(int(len(vals)/len(keys))):
                variables.append(vals[field_num*last_header_ind+0])

            # navigate to each variable page
            codebook = {}
            for variable in variables:
                variable_url = f"{url}&varName={variable}"
                driver.get(variable_url)
                time.sleep(self.sleep)
                table_css = driver.find_element_by_css_selector(
                    "body > table:nth-child(24) > tbody > tr:nth-child(2) > td:nth-child(3) > table:nth-child(5) > "
                    "tbody > tr > td > table:nth-child(3)"
                )
                var_table = table_css.text
                variable_dict = {}
                for row in var_table.split("\n"):
                    key_val = row.split(":")
                    variable_dict.update({key_val[0]: key_val[1].strip(" ")})
                
                # update codebook
                codebook[variable] = variable_dict
            
            # write to path
            UniversalUtilityFunctions.write_data_to_file(
                data=codebook,
                output_file_path=os.path.join(output_dir, f"{PUFId}_codebook"),
                output_file_format="json"
            )
            