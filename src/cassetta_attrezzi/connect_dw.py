import oracledb
import pandas as pd
import os
from dotenv import load_dotenv

def connessione_DW():
    load_dotenv()
    user = os.getenv("user")
    pssw= os.getenv("pssw")
    dsn = os.getenv("dsn")
    client_locale= "C:/Users/fabio.rosato2/instantclient_21_14"
    oracledb.init_oracle_client(client_locale) 
    connection = oracledb.connect(user=user, password=pssw, dsn=dsn)
    print("Connessione riuscita al DW")
    return connection

def getTabella( nome:str , schema="UNIBO_PSV"):
    connection = connessione_DW()

    cursor = connection.cursor()
    sql = f"select * from {schema}.{nome}"

    cursor.execute(sql)
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]

    df = pd.DataFrame(rows, columns=columns)
    
    cursor.close()
    connection.close()
    return df

