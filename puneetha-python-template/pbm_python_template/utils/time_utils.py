"""Time utilities."""

import datetime

from pbm_python_template.utils.constants.python_defaults import PythonDefaults
from pbm_python_template.utils.custom_logger import CustomLogger


class TimeUtils(CustomLogger):
    """Time utilities."""

    def __init__(self):
        """Instantiate time utilities."""
        CustomLogger.__init__(self, __name__)

        self.time_format = "%Y-%m-%d %H:%M:%S.%f"

    def get_time_now(self, time_name: str = "Start Time"):
        """
        Get current time in a format.

        Args:
            time_name (str): Start/End time name.

        Returns:
            time.

        """
        time = PythonDefaults().get_current_date().strftime(self.time_format)
        self.logger.info(f"{time_name} {time}")
        return time

    def get_start_time(self, log_text: str = ""):
        """
        Get start time in a format.

        Args:
            log_text (str): Log text.

        Returns:
            Start time.

        """
        return self.get_time_now(f"Start Time {log_text}")

    def get_end_time(self, log_text: str = ""):
        """
        Get end time in a format.

        Args:
            log_text (str): Log text.

        Returns:
            End time.
        """
        return self.get_time_now(f"End Time {log_text}")

    def log_time_diff(self, start_time: str, end_time: str, log_text: str = ""):
        """
        Log time difference.

        Args:
            start_time (str): Start time.
            end_time (str): End time.
            log_text (str): Log text.

        Returns:
            Time difference.

        """
        time_diff = datetime.datetime.strptime(end_time, self.time_format) \
                    - datetime.datetime.strptime(start_time, self.time_format)

        self.logger.info(f"Total time taken {log_text} {time_diff} ")
        return time_diff
