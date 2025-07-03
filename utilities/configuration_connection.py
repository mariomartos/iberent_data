from datetime import datetime
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import oracledb
import sqlparse

def connection_3411(user_input):
    tail = "&Encrypt=yes&Trusted_Connection=yes"
    if user_input.get("sqlserver3411_trust_cert", "no").lower() == "yes":
        tail += "&TrustServerCertificate=yes"

    conn_url = (
        f"mssql+pyodbc://@{user_input['sqlserver3411_host']}/{user_input['sqlserver3411_database']}"
        f"?driver={quote_plus(user_input['sqlserver3411_driver'])}{tail}")

    conn = create_engine(conn_url, fast_executemany=True).connect()
    print("✅ Conexión SQL Server 34.11")
    return conn

def connection_studio(user_input):
    host     = user_input["studio_host"]         # ibedata.database.windows.net
    catalog  = user_input["studio_database"]     # IbeData
    user     = user_input["studio_user"]
    pwd      = quote_plus(user_input["studio_password"])
    driver   = quote_plus(user_input["studio_driver"])

    tail = "&Encrypt=yes"                       # Azure exige TLS
    if user_input.get("studio_trust_cert", "no").lower() == "yes":
        tail += "&TrustServerCertificate=yes"   # normalmente innecesario en Azure

    conn_url = (
        f"mssql+pyodbc://{user}:{pwd}@{host}/{catalog}"
        f"?driver={driver}{tail}")

    conn = create_engine(conn_url, fast_executemany=True).connect()
    print("✅ Conexión Data Studio")
    return conn

def oracle_connection(user_input):
    oracledb.init_oracle_client(lib_dir=user_input["oracle_lib_dir"])
    
    dsn = oracledb.makedsn( user_input["oracle_host"],                
                            port = user_input.get("oracle_port"),                             
                            sid=user_input["oracle_sid"])              
    
    conn = oracledb.connect(user = user_input["oracle_user"],
                            password = user_input["oracle_password"],
                            dsn = dsn)
    print("✅ Oracle Connection")
    return conn

def play_sql_script(workspace,sql_path,connection):
    #Read file location
    sql_file_path = f"{workspace}\\{sql_path}" 
    sql_script = open(sql_file_path,'r')
    script = sql_script.read()
    script = sqlparse.format(script, strip_comments=True).strip()
    statements = sqlparse.split(script)

    for sql in statements:
        start_time = datetime.now()
        connection.execute(sql)
        end_time = datetime.now()
        print('Query Executed - Duration: {}'.format(end_time - start_time))