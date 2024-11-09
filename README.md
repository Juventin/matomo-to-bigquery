# Matomo to BigQuery

This project contains scripts and functions to load data from Matomo to BigQuery.

## Supported tables

- `Live.getLastVisitsDetails`, transformed and loaded into `matomo.visit` and `matomo.visit_detail` BigQuery tables.

## Project Structure

- `datamodel/` : Contains scripts to create the dataset and tables in BigQuery.
  - This is supposed to be run manually and only once.
- `initial_loading/` : Contains the script for the initial loading of Matomo data (this may take a while).
  - This is supposed to be run manually and only once.
- `daily_etl/` : Contains a Google Cloud Function for incremental loading of Matomo data.

## Deployment

Each folder contains specific instructions for deploying and configuring the scripts and functions.

### Configuration

Make sure to update the `.env` and `.env.yaml` files with your project variables before deploying.

### Prerequisites

- Google Cloud account with the necessary permissions (BigQuery Job user).
- JSON key for the service account.
- Matomo URL and Token.

## Usage

Follow the instructions in the subfolders to deploy and run the scripts and functions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
