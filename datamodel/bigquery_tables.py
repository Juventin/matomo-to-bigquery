import os
from dotenv import load_dotenv
from google.cloud import bigquery
from utils.bigquery import Table, create_dataset, create_table

load_dotenv()
PROJECT_ID = os.getenv("PROJECT_ID")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv(
    "APPLICATION_CREDENTIALS")

DATASET_NAME = "matomo"


class Visit(Table):
    def __init__(self):
        super().__init__(PROJECT_ID)

        self.dataset_id = DATASET_NAME
        self.table_name = "visit"
        self.date_partition = "serverdate"

        self.schema = [
            bigquery.SchemaField("idvisit", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("visitip", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("visitorid", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("fingerprint", "STRING", mode="NULLABLE"),
            bigquery.SchemaField(
                "goalconversions", "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField("sitecurrency", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("sitecurrencysymbol",
                                 "STRING", mode="NULLABLE"),
            bigquery.SchemaField("serverdate", "DATE", mode="NULLABLE"),
            bigquery.SchemaField("visitserverhour", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("lastactiontimestamp",
                                 "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField("lastactiondatetime",
                                 "DATETIME", mode="NULLABLE"),
            bigquery.SchemaField("sitename", "STRING", mode="NULLABLE"),
            bigquery.SchemaField(
                "servertimestamp", "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField("firstactiontimestamp",
                                 "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField("servertimepretty",
                                 "STRING", mode="NULLABLE"),
            bigquery.SchemaField("serverdatepretty",
                                 "STRING", mode="NULLABLE"),
            bigquery.SchemaField(
                "serverdateprettyfirstaction", "STRING", mode="NULLABLE"),
            bigquery.SchemaField(
                "servertimeprettyfirstaction", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("userid", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("visitortype", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("visitortypeicon", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("visitconverted", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("visitconvertedicon",
                                 "STRING", mode="NULLABLE"),
            bigquery.SchemaField("visitcount", "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField("visitecommercestatus",
                                 "STRING", mode="NULLABLE"),
            bigquery.SchemaField("visitecommercestatusicon",
                                 "STRING", mode="NULLABLE"),
            bigquery.SchemaField("dayssincefirstvisit",
                                 "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField("secondssincefirstvisit",
                                 "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField(
                "dayssincelastecommerceorder", "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField(
                "secondssincelastecommerceorder", "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField("visitduration", "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField("visitdurationpretty",
                                 "STRING", mode="NULLABLE"),
            bigquery.SchemaField("searches", "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField("actions", "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField("interactions", "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField("referrertype", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("referrertypename",
                                 "STRING", mode="NULLABLE"),
            bigquery.SchemaField("referrername", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("referrerkeyword", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("referrerkeywordposition",
                                 "STRING", mode="NULLABLE"),
            bigquery.SchemaField("referrerurl", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("referrersearchengineurl",
                                 "STRING", mode="NULLABLE"),
            bigquery.SchemaField("referrersearchengineicon",
                                 "STRING", mode="NULLABLE"),
            bigquery.SchemaField("referrersocialnetworkurl",
                                 "STRING", mode="NULLABLE"),
            bigquery.SchemaField("referrersocialnetworkicon",
                                 "STRING", mode="NULLABLE"),
            bigquery.SchemaField("languagecode", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("language", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("devicetype", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("devicetypeicon", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("devicebrand", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("devicemodel", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("operatingsystem", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("operatingsystemname",
                                 "STRING", mode="NULLABLE"),
            bigquery.SchemaField("operatingsystemicon",
                                 "STRING", mode="NULLABLE"),
            bigquery.SchemaField("operatingsystemcode",
                                 "STRING", mode="NULLABLE"),
            bigquery.SchemaField("operatingsystemversion",
                                 "STRING", mode="NULLABLE"),
            bigquery.SchemaField("browserfamily", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("browserfamilydescription",
                                 "STRING", mode="NULLABLE"),
            bigquery.SchemaField("browser", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("browsername", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("browsericon", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("browsercode", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("browserversion", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("totalecommercerevenue",
                                 "FLOAT", mode="NULLABLE"),
            bigquery.SchemaField("totalecommerceconversions",
                                 "FLOAT", mode="NULLABLE"),
            bigquery.SchemaField("totalecommerceitems",
                                 "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField("totalabandonedcartsrevenue",
                                 "FLOAT", mode="NULLABLE"),
            bigquery.SchemaField("totalabandonedcarts",
                                 "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField("totalabandonedcartsitems",
                                 "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField("events", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("continent", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("continentcode", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("country", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("countrycode", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("countryflag", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("region", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("regioncode", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("city", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("location", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("latitude", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("longitude", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("visitlocaltime", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("visitlocalhour", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("dayssincelastvisit",
                                 "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField("secondssincelastvisit",
                                 "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField("resolution", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("plugins", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("campaignid", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("campaigncontent", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("campaignkeyword", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("campaignmedium", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("campaignname", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("campaignsource", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("campaigngroup", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("campaignplacement",
                                 "STRING", mode="NULLABLE")
        ]


class VisitDetail(Table):
    def __init__(self):
        super().__init__(PROJECT_ID)

        self.dataset_id = DATASET_NAME
        self.table_name = "visit_detail"

        self.schema = [
            bigquery.SchemaField("id", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("idvisit", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("actiondetails_type",
                                 "STRING", mode="NULLABLE"),
            bigquery.SchemaField("actiondetails_url",
                                 "STRING", mode="NULLABLE"),
            bigquery.SchemaField("actiondetails_pagetitle",
                                 "STRING", mode="NULLABLE"),
            bigquery.SchemaField("actiondetails_pageidaction",
                                 "STRING", mode="NULLABLE"),
            bigquery.SchemaField("actiondetails_idpageview",
                                 "STRING", mode="NULLABLE"),
            bigquery.SchemaField(
                "actiondetails_servertimepretty", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("actiondetails_pageid",
                                 "STRING", mode="NULLABLE"),
            bigquery.SchemaField("actiondetails_pageloadtime",
                                 "STRING", mode="NULLABLE"),
            bigquery.SchemaField("actiondetails_timespent",
                                 "INTEGER", mode="NULLABLE"),
            bigquery.SchemaField(
                "actiondetails_timespentpretty", "STRING", mode="NULLABLE"),
            bigquery.SchemaField(
                "actiondetails_pageloadtimemilliseconds", "STRING", mode="NULLABLE"),
            bigquery.SchemaField(
                "actiondetails_pageviewposition", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("actiondetails_title",
                                 "STRING", mode="NULLABLE"),
            bigquery.SchemaField("actiondetails_subtitle",
                                 "STRING", mode="NULLABLE"),
            bigquery.SchemaField("actiondetails_icon",
                                 "STRING", mode="NULLABLE"),
            bigquery.SchemaField("actiondetails_iconsvg",
                                 "STRING", mode="NULLABLE"),
            bigquery.SchemaField("actiondetails_timestamp",
                                 "INTEGER", mode="NULLABLE")
        ]


if __name__ == "__main__":

    create_dataset(DATASET_NAME, PROJECT_ID)
    create_table(Visit())
    create_table(VisitDetail())
