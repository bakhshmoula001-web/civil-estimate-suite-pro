"""
Civil Estimate Suite Pro v3.0
Application Controller

Author : Moula Bakhsh
"""

from app.core.theme import Theme
from app.database.schema import DatabaseSchema
from app.core.window_manager import WindowManager


class CivilEstimateApplication:
    """
    Main Application Controller
    """

    def __init__(self):

        # Load Theme
        Theme.load()

        # Initialize Database
        DatabaseSchema().initialize()

        # Launch Main Window
        self.window = WindowManager()

    def run(self):
        self.window.mainloop()