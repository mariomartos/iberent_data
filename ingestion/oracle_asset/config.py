import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

# Origen (Oracle)
ORA_USER = os.getenv("ORA_USER")
ORA_PASS = os.getenv("ORA_PASS")
ORA_HOST = os.getenv("ORA_HOST")
ORA_PORT = os.getenv("ORA_PORT", "1521")
ORA_DB   = os.getenv("ORA_DB")
ADAPTER_ORACLE = "oracle+cx_oracle"

ORA_CONN = (
    f"{ADAPTER_ORACLE}://{ORA_USER}:{ORA_PASS}"
    f"@{ORA_HOST}:{ORA_PORT}/{ORA_DB}"
)
source_engine = create_engine(ORA_CONN)


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
