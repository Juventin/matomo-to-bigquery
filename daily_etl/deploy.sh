echo "Have you updated the .env and .env.yaml file ? (Y/n)"
read greenlight

if [ "$greenlight" == "Y" ]; then

    source matomo-to-bigquery/etl/.env

    gcloud config set account $ACCOUNT_EMAIL
    gcloud config set project $PROJECT_ID

    gcloud functions deploy matomo-to-bigquery \
        --gen2 \
        --region=$LOCATION \
        --source=matomo-to-bigquery/etl/cloud-function \
        --trigger-http \
        --entry-point=etl \
        --runtime=python311 \
        --timeout=3600 \
        --memory=2Gi \
        --ingress-settings=all \
        --no-allow-unauthenticated \
        --env-vars-file=matomo-to-bigquery/etl/.env.yaml

    gcloud scheduler jobs create http matomo-to-bigquery \
        --uri="https://$LOCATION-$PROJECT_ID.cloudfunctions.net/matomo-to-bigquery" \
        --schedule=$SCHEDULE \
        --time-zone=Europe/Paris \
        --location=$LOCATION \
        --http-method=POST \
        --attempt-deadline=30m \
        --oidc-service-account-email="workflows@$PROJECT_ID.iam.gserviceaccount.com"

    gcloud functions add-iam-policy-binding matomo-to-bigquery \
        --member="serviceAccount:workflows@$PROJECT_ID.iam.gserviceaccount.com" \
        --role="roles/run.invoker" \
        --region=$LOCATION

    gcloud functions add-iam-policy-binding matomo-to-bigquery \
        --member="serviceAccount:workflows@$PROJECT_ID.iam.gserviceaccount.com" \
        --role="roles/cloudfunctions.invoker" \
        --region=$LOCATION
fi