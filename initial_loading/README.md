# Matomo to BigQuery

This repository contains a script for the initial loading of Matomo data into Google BigQuery.

This scipt is intended to be run manually and only once, in order to load historical data from Matomo into BigQuery.

## Prerequisites

Ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)

Ensure you have created the BigQuery dataset and tables using the `datamodel` scripts before running this script.

## Installation

1. Install the required Python packages:

   ```sh
   pip install -r requirements.txt
   ```

2. Create a `.env` file in this directory with the following content:
   ```sh
   MATOMO_URL="YOUR_MATOMO_URL"
   MATOMO_TOKEN="YOUR_MATOMO_TOKEN"
   PROJECT_ID="YOUR_PROJECT_ID"
   APPLICATION_CREDENTIALS="PATH_TO_JSON_KEY"
   ```

## Usage

To run the script, execute the following command:

```sh
python ./initial_loading/run.py
```

## Details

The `initial_loading` script performs the following steps:

1. **Load Environment Variables**: Reads configuration from the `.env` file.
2. **Set Google Credentials**: Sets the Google Cloud credentials for authentication.
3. **Process Data**: Extracts data from Matomo, transforms it, and loads it into BigQuery.
   - The data is processed in chunks to handle large datasets efficiently.
   - The script iterates over the data by date and offset to ensure all records are processed.
4. **Error Handling**: The script includes basic error handling to manage issues during data extraction, transformation, or loading.

Ensure that the `.env` file is correctly configured with your Matomo and Google Cloud details before running the script.
