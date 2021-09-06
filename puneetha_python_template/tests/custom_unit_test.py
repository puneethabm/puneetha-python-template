"""Python Test Utility."""

import unittest

from puneetha_python_template.utils.custom_logger import CustomLogger


class CustomUnitTest(unittest.TestCase):
    """Python Test Utility."""

    @classmethod
    def setUpClass(cls):
        """Set up variables."""
        cls.logger = CustomLogger("CustomUnitTest").logger
