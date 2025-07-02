from sqlalchemy import create_engine
from urllib.parse import quote_plus

def salesforce_connection(user_input: dict):
    host     = user_input["salesforce_host"]
    database = user_input["salesforce_database"]
    driver   = user_input["salesforce_driver"]

    extras = "&Encrypt=yes"
    if user_input.get("salesforce_trust_cert", "no").lower() == "yes":
        extras += "&TrustServerCertificate=yes"

    # URL con Trusted_Connection=yes (Windows Authentication)
    conn_url = (
        f"mssql+pyodbc://@{host}/{database}"
        f"?driver={driver}{extras}&Trusted_Connection=yes"
    )

    engine = create_engine(conn_url, fast_executemany=True)
    conn   = engine.connect()
    print("✅ Connection SQL Server – Salesforce_DB")
    return conn

def sgm_connection(user_input: dict):
    host     = user_input["sgm_host"]
    database = user_input["sgm_database"]
    driver   = user_input["sgm_driver"]

    extras = "&Encrypt=yes"
    if user_input.get("sgm_trust_cert", "no").lower() == "yes":
        extras += "&TrustServerCertificate=yes"

    # URL con Trusted_Connection=yes (Windows Authentication)
    conn_url = (
        f"mssql+pyodbc://@{host}/{database}"
        f"?driver={driver}{extras}&Trusted_Connection=yes"
    )

    engine = create_engine(conn_url, fast_executemany=True)
    conn   = engine.connect()
    print("✅ Connection SQL Server – SGM")
    return conn













def mango_mysql_connection(user_input):
    #Connection variables
    user = user_input["mysql_user"]
    password = user_input["mysql_password"]
    host = user_input["mysql_host"]
    database = user_input["mysql_database"]
    
    #Connection generation
    mango_mysql_engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")    
    mango_mysql_conn = mango_mysql_engine.connect()
    print('Connection MySQL')
    return mango_mysql_conn

def oracle_connection(user_input):
    #Connection variables
    user = user_input["oracle_username"]
    password = user_input["oracle_password"]
    host = user_input["oracle_localhost"]
    oracle_orclpdb = user_input["oracle_orclpdb"]
    
    #Connection generation
    oracle_connnection = oracledb.connect(user=user,
                                          password=password, 
                                          dsn=f"{host}/{oracle_orclpdb}")

    print('Connection Oracle')
    return oracle_connnection

def oracle_mango_pro_connection(user_input):
    #Connection variables
    user = user_input["oracle_pro_username"]
    password = user_input["oracle_pro_password"]
    host = user_input["oracle_pro_localhost"]
    oracle_orclpdb = user_input["oracle_pro_orclpdb"]
    
    #Connection generation
    oracle_connnection = oracledb.connect(user=user,
                                          password=password, 
                                          dsn=f"{host}/{oracle_orclpdb}")

    print('Connection Pro Oracle')
    return oracle_connnection

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
        
    end_time = datetime.now()
    print('Mango Views - Updated - Duration: {}'.format(end_time - start_time))