"""
=========================================================
 Civil Estimate Suite Pro v3.0
---------------------------------------------------------
 Settings Manager
---------------------------------------------------------
Author  : Moula Bakhsh
Version : 3.0.0
=========================================================
"""

import json
from pathlib import Path

from app.core.constants import ROOT_DIR


class Settings:
    """
    Application Settings Manager
    """

    SETTINGS_FILE = ROOT_DIR / "settings.json"

    DEFAULT_SETTINGS = {
        "theme": "light",
        "color_theme": "blue",
        "currency": "PKR",
        "default_unit": "m³",
        "company_name": "Moula Bakhsh Engineering Solutions",
        "auto_save": True,
        "window_state": "zoomed"
    }

    @classmethod
    def load(cls):
        """
        Load settings from settings.json.
        If file does not exist, create it with default values.
        """

        if not cls.SETTINGS_FILE.exists():
            cls.save(cls.DEFAULT_SETTINGS)
            return cls.DEFAULT_SETTINGS.copy()

        try:
            with open(cls.SETTINGS_FILE, "r", encoding="utf-8") as file:
                return json.load(file)

        except Exception:
            cls.save(cls.DEFAULT_SETTINGS)
            return cls.DEFAULT_SETTINGS.copy()

    @classmethod
    def save(cls, settings):
        """
        Save settings to settings.json.
        """

        with open(cls.SETTINGS_FILE, "w", encoding="utf-8") as file:
            json.dump(settings, file, indent=4)

    @classmethod
    def get(cls, key):
        """
        Get a single setting.
        """

        settings = cls.load()
        return settings.get(key)

    @classmethod
    def set(cls, key, value):
        """
        Update one setting.
        """

        settings = cls.load()
        settings[key] = value
        cls.save(settings)