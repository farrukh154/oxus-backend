from django.conf import settings

MSSQL_DB_CON = settings.MSSQL_DB_CON

connection_string = f"""
    DRIVER={{{MSSQL_DB_CON['DRIVER_NAME']}}};
    SERVER={MSSQL_DB_CON['SERVER_NAME']};
    DATABASE={MSSQL_DB_CON['DB_NAME']};
    Trust_connection=yes;
    uid={MSSQL_DB_CON['LOGIN']};
    pwd={MSSQL_DB_CON['PASSWORD']};
    Encrypt=no;
"""

