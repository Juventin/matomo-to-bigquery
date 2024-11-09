# Matomo to BigQuery

This ETL is a Google Cloud Function triggered by a Google Schedule.

This scipt is intended to be run manually and only once, in order to create the BigQuery dataset and tables.

## Prerequisites

Ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)

Create a deployer Service Account with the necessary roles and save a JSON key.

## Installation

1. Install the required Python packages from the root directory of this reposotory:

   ```sh
   pip install -r requirements.txt
   ```

2. Create a `.env` file in this directory with the following content:
   ```sh
   APPLICATION_CREDENTIALS="PATH_TO_JSON_KEY"
   PROJECT_ID="YOUR_PROJECT_ID"
   ```

## Usage :

Run the following in your terminal:

```sh
sh ./datamodel/deploy.sh
```
