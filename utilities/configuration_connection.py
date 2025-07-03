from sqlalchemy import create_engine
from urllib.parse import quote_plus
import oracledb

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

def oracle_connection(cfg):
    user     = cfg["oracle_user"]
    password = cfg["oracle_password"]
    host     = cfg["oracle_host"]
    port     = cfg.get("oracle_port", 1521)

    # --- Modo thick opcional -----------------------------------------
    if cfg.get("oracle_mode", "thin").lower() == "thick":
        oracledb.init_oracle_client(lib_dir=cfg.get("oracle_lib_dir"))

    # --- Construir DSN según SID o Service ---------------------------
    if "oracle_sid" in cfg:
        dsn = oracledb.makedsn(host, port, sid=cfg["oracle_sid"])
    elif "oracle_service" in cfg:
        dsn = oracledb.makedsn(host, port, service_name=cfg["oracle_service"])
    else:
        raise KeyError("Debes definir 'oracle_sid' o 'oracle_service' en el YAML")

    conn = oracledb.connect(user=user, password=password, dsn=dsn)
    print("✅ Connection Oracle –", dsn)
    return conn
