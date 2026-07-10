"""
ANURAG ERP PRO AI
Application Configuration
"""

from pathlib import Path

# ---------------------------------------------------
# Project Paths
# ---------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent.parent

APP_DIR = BASE_DIR / "app"
ASSETS_DIR = BASE_DIR / "assets"
LOG_DIR = BASE_DIR / "logs"
BACKUP_DIR = BASE_DIR / "backup"

# ---------------------------------------------------
# Application Information
# ---------------------------------------------------

APP_NAME = "ANURAG ERP PRO AI"
APP_EDITION = "Enterprise Edition"
APP_VERSION = "2.0.0"

# ---------------------------------------------------
# Database
# ---------------------------------------------------

DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "anurag_erp"
DB_USER = "postgres"
DB_PASSWORD = ""

# ---------------------------------------------------
# Theme
# ---------------------------------------------------

DEFAULT_THEME = "light"

# ---------------------------------------------------
# Company
# ---------------------------------------------------

DEFAULT_COMPANY = "ANURAG TRADERS"

# ---------------------------------------------------
# Create Required Folders
# ---------------------------------------------------

LOG_DIR.mkdir(exist_ok=True)
BACKUP_DIR.mkdir(exist_ok=True)