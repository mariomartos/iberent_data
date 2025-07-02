# ingestion/sql_server_salesforce/test_connection.py

import os
import sys
import pandas as pd

# Añade el root del proyecto al PYTHONPATH para que funcione el package import
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
sys.path.insert(0, project_root)

from ingestion.sql_server_salesforce.config import source_engine

def main():
    query = "SELECT TOP 10 * FROM [dbo].[Contract__c]"
    try:
        df = pd.read_sql(query, source_engine)
        print(df)
        print(f"\n[OK] Se han recuperado {len(df)} registros de Contract__c")
    except Exception as e:
        print(f"[ERROR] al ejecutar la consulta: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
