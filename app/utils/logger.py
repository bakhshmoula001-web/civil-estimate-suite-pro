import logging
from pathlib import Path

class AppLogger:
    LOG_FILE = Path("logs/application.log")

    @classmethod
    def get_logger(cls):
        cls.LOG_FILE.parent.mkdir(exist_ok=True)
        logging.basicConfig(
            filename=cls.LOG_FILE,
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )
        return logging.getLogger("CivilEstimateSuite")
