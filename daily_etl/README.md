# Matomo to BigQuery

This ETL is a **Google Cloud Function** triggered by **Google Cloud Scheduler**.

## Deploy :

1. Update `.env.yaml` and `.env` with project variables
2. Create a `workflows@$PROJECT_ID.iam.gserviceaccount.com` service account
3. Run `sh matomo-to-bigquery/etl/deploy.sh`

## Env files

### .env
```sh
SCHEDULE="0 6 * * *"
ACCOUNT_EMAIL="YOUR_EMAIL"
PROJECT_ID="YOUR_PROJECT_ID"
LOCATION="CLOUD_FUNCTION_LOCATION"
```

### .env.yaml
```yaml
MATOMO_URL: YOUR_MATOMO_URL
MATOMO_TOKEN: YOUR_MATOMO_TOKEN
PROJECT_ID: YOUR_PROJECT_ID
```