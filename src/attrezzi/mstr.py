from dotenv import load_dotenv
import os
from datetime import date
from mstrio.project_objects.report import Report
from mstrio.connection import Connection

def connectMSTR():
    load_dotenv()
    BASE_URL = os.getenv("BASE_URL")
    MSTR_USERNAME= os.getenv("MSTR_USERNAME")
    MSTR_PASSWORD = os.getenv("MSTR_PASSWORD")
    PROJECT_ID = os.getenv("PROJECT_ID")
    conn = Connection ( BASE_URL, MSTR_USERNAME, MSTR_PASSWORD, project_id= PROJECT_ID)
    conn.connect()
    return conn

def to_pandas(id, export=False, limit= None):
    conn = connectMSTR()
    report = Report(conn, id)
    df= report.to_dataframe(limit=limit)
    if export:
        name = report.get("name")
        df.to_excel(f"DWH_{name}_{date.today()}.xlsx", index=False)
    return df
