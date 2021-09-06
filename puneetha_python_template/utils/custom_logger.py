"""Logger Utility."""

import os
import sys

from loguru import logger

from puneetha_python_template.utils.constants.env_variable_mapper import EnvironmentVariableMapper
from puneetha_python_template.utils.constants.project_defaults import ProjectDefaults


class CustomLogger:
    """Custom Logger."""

    def __init__(self, logger_name):
        """Initialise logger name."""
        self.logger_name = logger_name

        log_format: str = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | " \
                          "<level>{level: <8}</level> | " \
                          "<green>[{extra[logger_name]}]</green> | " \
                          "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"

        self.logger: logger = logger
        self.logger.remove()  # All configured handlers are removed

        log_file_path: str = os.path.join(EnvironmentVariableMapper.PBM_LOG_FILE_PATH.value)

        config: dict = {
            "handlers": [
                {
                    "sink": sys.stdout,
                    "format": log_format,
                },
                {
                    "sink": log_file_path,
                    "format": log_format,
                    "rotation": "12:00",
                    "retention": "30 days",
                    "encoding": ProjectDefaults.ENCODING.value
                }
            ],
            "extra": {"logger_name": self.logger_name}
        }

        self.logger.configure(**config)
