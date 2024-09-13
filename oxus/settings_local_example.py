from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "oxus-backend/db.sqlite3",
    }
}

MSSQL_DB_CON = {
    "DRIVER_NAME": "SQL SERVER",
    "SERVER_NAME": "localhost",
    "DB_NAME": "abacus",
    "LOGIN": "sa",
    "PASSWORD": "abacus",
}

CRIF_URL = 'https://a2atest.cibt.tj' # CIBT
CRIF_LOGIN  = 'QOQE2305'
CRIF_PASSWORD  = 'grjQj2ORU3'

BASE_URL = "http://127.0.0.1:8000/"

GENERATED_REPORTS_DIR = 'gen_reports'
