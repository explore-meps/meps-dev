import os
import shutil
import time

from os.path import expanduser
from selenium import webdriver

from meps_db.components.reference import (
    DATA_FILES_BASE_URL,
    DATA_STATS_BASE_URL,
    DATA_FILES_YEARS,
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


class ScrapMEPS:
    """ Web scrapper class. Uses Selenium to navigate to the MEPS AHRQ Data files page in browser. Downloads dat and
    txt files to the specified input file location. Requires a chromedriver associated with the version of chrome
    running on the local machine. Follow instructions on https://chromedriver.chromium.org/downloads to identify the
    driver suited for the local machine. """

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

        self.get_data_files(folder="consolidated", year_lookup=FYCDF_PUF_LOOKUP)
        self.get_data_files(folder="population_characteristics", year_lookup=FYPCDF_PUF_LOOKUP)
        self.get_data_files(folder="medical_conditions", year_lookup=MCDF_PUF_LOOKUP)
        self.get_data_files(folder="prescribed_medicines", year_lookup=PMDF_PUF_LOOKUP)

        self.get_data_files(folder="dental_visits", year_lookup=DVDF_PUF_LOOKUP)
        self.get_data_files(folder="other_medical_expenses", year_lookup=OMEDF_PUF_LOOKUP)
        self.get_data_files(folder="hospital_inpatient_stays", year_lookup=HISDF_PUF_LOOKUP)
        self.get_data_files(folder="emergency_room_visits", year_lookup=ERVDF_PUF_LOOKUP)
        self.get_data_files(folder="outpatient_visits", year_lookup=OVDF_PUF_LOOKUP)
        self.get_data_files(folder="office_based_visits", year_lookup=OBMPVDF_PUF_LOOKUP)
        self.get_data_files(folder="home_health", year_lookup=HHDF_PUF_LOOKUP)

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
            driver.get(f"{DATA_FILES_BASE_URL}{year_lookup[year]}dat.zip")
            driver.get(f"{DATA_STATS_BASE_URL}{year_lookup[year]}/{year_lookup[year]}su.txt")
            text = driver.find_element_by_css_selector("body > pre").text
            with open(f"{download_dir}/{year_lookup[year]}su.txt", 'w') as f:
                f.write(text)

        time.sleep(self.sleep)
        driver.close()

        self.validate_downloads(download_dir=download_dir, year_lookup=year_lookup, years=self.years)

    @staticmethod
    def validate_downloads(download_dir, year_lookup, years):
        """ Takes a download path, a year to PUF no. lookup and the targeted years. Validates that all expected files
        have been downloaded.
        """

        downloads = os.listdir(download_dir)
        missing_files = []
        for year, puf_no in year_lookup.items():
            if year in years:
                if f"{puf_no}dat.zip" not in downloads:
                    missing_files.append(f"{puf_no}dat.zip")
                if f"{puf_no}su.txt" not in downloads:
                    missing_files.append(f"{puf_no}dat.zip")
       
        if len(missing_files) > 0:
            raise AssertionError(
                f"The following files were not able to be fetched {', '.join(missing_files)} check if the PUF "
                f"numbers have been updated"
            )
