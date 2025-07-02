from sqlalchemy import create_engine
import teradatasql
import oracledb
import snowflake.connector 
import sqlparse
from datetime import datetime


def teradata_connection(user_input):
    #Connection variables
    user = user_input["teradata_user"]
    password = user_input["teradata_password"]
    host = user_input["teradata_host"]
    
    #Connection generation
    teradata_connection = teradatasql.connect(host=host, user=user, password=password)                                   
    print('Connection Teradata')
    return teradata_connection

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

def snowflake_connection(user_input):
    #Connection variables
    user = user_input["snowflake_user"]
    password = user_input["snowflake_password"]
    host = user_input["snowflake_host"]
    account = user_input["snowflake_account"]

    #Connection generation
    snowflake_connnection = snowflake.connector.connect(authenticator='externalbrowser',
                                                        host=host, 
                                                        user=user,
                                                        password=password,
                                                        account=account)

    print('Connection Snowflake -- Will prompt a page login connection')
    return snowflake_connnection