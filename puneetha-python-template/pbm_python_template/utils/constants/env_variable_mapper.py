"""Environment variables."""

from enum import Enum

from envparse import env


class EnvironmentVariableMapper(Enum):
    """Environment variables mapping."""

    # Options can be "DEV", "TEST", "PREPROD", "PROD"
    PBM_ENV_NAME = env.str("PBM_ENV_NAME", default="DEV")

    PBM_MODULE_NAME = env.str("PBM_MODULE_NAME", default="pbm_python_template")

    PBM_LOG_CONFIG_FILE_NAME = env.str("PBM_LOG_CONFIG_FILE_NAME", default="logging.conf")

    PBM_LOG_FILE_PATH = env.str("PBM_LOG_FILE_PATH", default="/var/log/pbm-python-template.log")

    # Options can be "INFO", "DEBUG", "WARNING", "ERROR"
    LOGURU_LEVEL = env.str("LOGURU_LEVEL", default="INFO")
