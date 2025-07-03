from configuration_connection import connection_3411, connection_studio, connection_oracle

def get_columns_3411(table_name: str, catalog: str) -> list[str]:
    conn = connection_3411()
    sql = f"""SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_CATALOG = '{catalog}' AND TABLE_NAME = '{table_name}' ORDER BY ORDINAL_POSITION"""
    cols = [row.COLUMN_NAME for row in conn.execute(sql).fetchall()]
    conn.close()
    return cols

def get_columns_studio(table_name: str, catalog: str) -> list[str]:
    conn = connection_studio()
    sql = f"""SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_CATALOG = '{catalog}' AND TABLE_NAME = '{table_name}' ORDER BY ORDINAL_POSITION"""
    cols = [row.COLUMN_NAME for row in conn.execute(sql).fetchall()]
    conn.close()
    return cols

def get_columns_oracle(table_name: str, owner: str) -> list[str]:
    conn = connection_oracle()
    sql = f"""SELECT COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE OWNER = '{owner.upper()}' AND TABLE_NAME = '{table_name.upper()}' ORDER BY COLUMN_ID"""
    cols = [row.COLUMN_NAME for row in conn.execute(sql).fetchall()]
    conn.close()
    return cols