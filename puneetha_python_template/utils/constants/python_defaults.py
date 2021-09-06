"""Python Default Formats."""

import datetime

from puneetha_python_template.utils.custom_logger import CustomLogger


class PythonDefaults(CustomLogger):
    """Python Defaults."""

    def __init__(self):
        """Instantiate Python Defaults."""
        self.app_name = "Python Defaults"

        CustomLogger.__init__(self, __name__)

    @staticmethod
    def get_timestamp_format() -> str:
        """
        Get timestamp format.

        Returns:
            str: Timestamp format.

        """
        return "%Y-%m-%dT%H:%M:%S.%f"

    @staticmethod
    def get_current_date() -> datetime.date:
        """
        Get Current date.

        Returns:
            datetime.date: Current date.

        """
        return datetime.datetime.utcnow()
