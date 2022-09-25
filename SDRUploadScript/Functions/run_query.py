import Functions.Credentials.credentials_SQL as credsql
import mysql.connector as ms
from mysql.connector import Error
from mysql.connector import errorcode 
import pandas as pd
import os


def run_query(query, database):
    '''Executes SQL query by connecting to the datamart.

    Parameters
    ----------
    query : file type (e.g., sql, txt)
        SQL query
    database : str
        Datamart schema

    Returns
    -------
    dataframe
        query results are stored in a pandas dataframe
    '''
    
    global data

    # Connect to the datamart.
    cert_path=os.path.expanduser('/Users/jnichols/Python Files/account-matching-script/Functions/Certificates/rds-combined-ca-bundle.pem')
    cnx = ms.connect(
        host=credsql.host,
        port=credsql.port,
        user=credsql.username,
        password=credsql.password,
        database=database,
        ssl_ca=cert_path
        )

    # Run query and save as a dataframe.
    data = pd.read_sql(query, cnx)

    # Close connection.
    cnx.close()
    return data