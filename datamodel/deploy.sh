echo "Have you updated the .env file ? (Y/n)"
read greenlight

if [ "$greenlight" == "Y" ]; then
   python ./datamodel/bigquery_tables.py
fi
