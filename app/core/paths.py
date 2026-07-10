"""
Application Paths
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent

ASSETS = ROOT / "assets"
LOGS = ROOT / "logs"
BACKUP = ROOT / "backup"

ICONS = ASSETS / "icons"
IMAGES = ASSETS / "images"
LOGO = ASSETS / "logo"
FONTS = ASSETS / "fonts"