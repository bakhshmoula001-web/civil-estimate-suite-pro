"""
=========================================================
 Civil Estimate Suite Pro v3.0
---------------------------------------------------------
 Global Constants
---------------------------------------------------------
Author  : Moula Bakhsh
Version : 3.0.0
=========================================================
"""

from pathlib import Path


# =========================================================
# Software Information
# =========================================================

APP_NAME = "Civil Estimate Suite Pro"

APP_VERSION = "3.0.0"

APP_AUTHOR = "Moula Bakhsh"

COMPANY_NAME = "A Badshah Technologies"


# =========================================================
# Folder Paths
# =========================================================

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

APP_DIR = ROOT_DIR / "app"

DATA_DIR = ROOT_DIR / "data"

ASSETS_DIR = ROOT_DIR / "assets"

DOCS_DIR = ROOT_DIR / "docs"

TESTS_DIR = ROOT_DIR / "tests"


# =========================================================
# Database
# =========================================================

DATABASE_NAME = "civil_estimate.db"

DATABASE_PATH = DATA_DIR / DATABASE_NAME


# =========================================================
# Assets
# =========================================================

ICON_PATH = ASSETS_DIR / "icons" / "app.ico"

LOGO_PATH = ASSETS_DIR / "images" / "logo.png"

SPLASH_IMAGE = ASSETS_DIR / "images" / "splash.png"


# =========================================================
# Reports
# =========================================================

EXPORT_FOLDER = ROOT_DIR / "exports"

EXCEL_REPORT = EXPORT_FOLDER / "BOQ_Report.xlsx"

PDF_REPORT = EXPORT_FOLDER / "BOQ_Report.pdf"


# =========================================================
# Window
# =========================================================

DEFAULT_WIDTH = 1400

DEFAULT_HEIGHT = 800

MIN_WIDTH = 1200

MIN_HEIGHT = 700


# =========================================================
# Engineering Units
# =========================================================

UNITS = [
    "m",
    "m²",
    "m³",
    "Cft",
    "Kg",
    "Ton",
    "Nos",
]


# =========================================================
# Supported Modules
# =========================================================

MODULES = [
    "Project",
    "BOQ",
    "Excavation",
    "PCC",
    "Brickwork",
    "Plaster",
    "Steel",
    "Material Report",
    "Cost Report",
    "Excel Export",
    "PDF Export",
]