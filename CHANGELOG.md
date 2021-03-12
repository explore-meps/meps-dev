# Change Log

All noteable changes to this project are documented in this file. This project adheres to
[Semantic Versioning](https://semver.org/). See [Keep a CHANGELOG](https://keepachangelog.com/en/1.0.0/) for reference.

## v0.0.0 - 2021-03-08

Features

- Built ScrapMEPSSSP class and mgmt command for fetching ssp files from the MEPS data center
- Built ScrapMEPSCodebook class and mgmt command for fetching codebook data from the MEPS data center
- Rebuilt ScrapMEPSSSP as ScrapMEPS, now fetches .dat files and associated SAS .txt files
- Built ComponentPopulator, extracts ascii text from .dat files and orders according to the associated SAS .txt files
- Built SQLite3 table which contains all models associated with an .dat file
- Built model populating and depopulating management commands
- Made server admin page accessible

Updates:

- none

Fixes:

- none

Deployment Instructions:

- none
