import pandas as pd
from datetime import datetime
from utilities.configuration_connection import oracle_connection
from utilities.yaml_reader import generate_user_input, generate_sql_script

workspace = r"X:\iberent_data"
start_time = datetime.now()

# 1) Cargar configuración
user_input = generate_user_input(workspace)

# 2) Conexión a la BD de Salesforce
ora_conn = oracle_connection(user_input)

# 3) Probar la conexión
df = pd.read_sql("SELECT * FROM IBERICA.BAILLEUR", ora_conn)
print(df.head())

ora_conn.close()
print(f"✅ Conexión probada en {datetime.now() - start_time}")
