import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

# Origen (Salesfoce_DB)
SF_USER    = os.getenv("SF_USER")
SF_PASS    = os.getenv("SF_PASS")
SF_HOST    = os.getenv("SF_HOST")
SF_PORT    = os.getenv("SF_PORT", "1433")
SF_NAME    = os.getenv("SF_NAME")
SF_DRIVER  = os.getenv("SF_DRIVER", "ODBC Driver 17 for SQL Server")
RAW_SCHEMA = os.getenv("SF_SCHEMA", "raw")
driver_param = SF_DRIVER.replace(" ", "+")
ADAPTER_MSSQL = "mssql+pyodbc"

SF_CONN = (
    f"{ADAPTER_MSSQL}://{SF_USER}:{SF_PASS}"
    f"@{SF_HOST}:{SF_PORT}/{SF_NAME}"
    f"?driver={driver_param}"
)
source_engine = create_engine(SF_CONN, fast_executemany=True)

# Destino (SQL Server)
DB_USER    = os.getenv("DB_USER")
DB_PASS    = os.getenv("DB_PASS")
DB_HOST    = os.getenv("DB_HOST")
DB_PORT    = os.getenv("DB_PORT", "1433")
DB_NAME    = os.getenv("DB_NAME")
DB_DRIVER  = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")
RAW_SCHEMA = os.getenv("DB_SCHEMA", "raw")
driver_param = DB_DRIVER.replace(" ", "+")
ADAPTER_MSSQL = "mssql+pyodbc"

DB_CONN = (
    f"{ADAPTER_MSSQL}://{DB_USER}:{DB_PASS}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    f"?driver={driver_param}"
)
dest_engine = create_engine(DB_CONN, fast_executemany=True)