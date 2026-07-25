"""
Civil Estimate Suite Pro v3.0

Theme Manager
---------------------------------
Centralized theme configuration for
the entire application.

Author : Moula Bakhsh
Version : 3.0
"""

import customtkinter as ctk
from app.core.settings import Settings

Settings.set("theme", "dark")

class Theme:
    """
    Global Theme Configuration
    """

    # ----------------------------------
    # Appearance
    # ----------------------------------

    APPEARANCE_MODE = "light"
    COLOR_THEME = "blue"

    # ----------------------------------
    # Window
    # ----------------------------------

    WINDOW_TITLE = "Civil Estimate Suite Pro v3.0"

    WINDOW_WIDTH = 1400
    WINDOW_HEIGHT = 800

    MIN_WIDTH = 1200
    MIN_HEIGHT = 700

    # ----------------------------------
    # Fonts
    # ----------------------------------

    FONT_FAMILY = "Segoe UI"

    TITLE_FONT = (FONT_FAMILY, 30, "bold")
    HEADING_FONT = (FONT_FAMILY, 22, "bold")
    SUBTITLE_FONT = (FONT_FAMILY, 18)
    BODY_FONT = (FONT_FAMILY, 14)
    SMALL_FONT = (FONT_FAMILY, 12)

    # ----------------------------------
    # Colors
    # ----------------------------------

    PRIMARY = "#1F6AA5"
    SUCCESS = "#2E8B57"
    WARNING = "#F4A300"
    DANGER = "#D32F2F"

    TEXT = "#202020"

    SIDEBAR = "#E8EEF5"

    BACKGROUND = "#F8F9FA"

    CARD = "#FFFFFF"

    BORDER = "#D6D6D6"

    # ----------------------------------
    # Button Size
    # ----------------------------------

    BUTTON_WIDTH = 150
    BUTTON_HEIGHT = 40

    # ----------------------------------
    # Entry
    # ----------------------------------

    ENTRY_WIDTH = 220

    # ----------------------------------
    # Table
    # ----------------------------------

    TABLE_ROW_HEIGHT = 28

    @classmethod
    def load(cls):
        """
        Apply global theme.
        """
        ctk.set_appearance_mode(cls.APPEARANCE_MODE)
        ctk.set_default_color_theme(cls.COLOR_THEME)