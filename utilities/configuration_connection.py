from datetime import datetime
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import oracledb
import sqlparse

def connection_3411(user_input):
    tail = "&Encrypt=yes&Trusted_Connection=yes"
    if user_input.get("salesforce_trust_cert", "no").lower() == "yes":
        tail += "&TrustServerCertificate=yes"

    conn_url = (
        f"mssql+pyodbc://@{user_input['salesforce_host']}/{user_input['salesforce_database']}"
        f"?driver={quote_plus(user_input['salesforce_driver'])}{tail}")

    conn = create_engine(conn_url, fast_executemany=True).connect()
    print("✅ Conexión SQL Server 34.11")
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



#Functions to review
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

def play_sql_view_script(workspace,connection):
    #Read file location
    #Mango Views - master level 
    workspace = workspace.replace('\\online_operations_project','')
    sql_file_path = f"{workspace}\\mango_local_views.sql" 
    sql_script = open(sql_file_path,'r')
    script = sql_script.read()
    script = sqlparse.format(script, strip_comments=True).strip()
    statements = sqlparse.split(script)

    start_time = datetime.now()
    
    for sql in statements:
        #% Escape character issue - replace all the cases with 2 % instead of 1
        sql = sql.replace('%','%%')
        try:
            connection.execute(sql)
        except:
            print('Error - View Query failed to update')   