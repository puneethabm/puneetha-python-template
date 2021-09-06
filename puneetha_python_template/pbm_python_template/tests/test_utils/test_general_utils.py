"""Test - General Utilities."""

from parameterized import parameterized

from puneetha_python_template.pbm_python_template.tests.custom_unit_test import CustomUnitTest
from puneetha_python_template.pbm_python_template.utils.general_utils import GeneralUtils


class TestGeneralUtils(CustomUnitTest):
    """General Utilities tests."""

    @parameterized.expand(
        [
            (
                "Basic test",
                {"key1": "val1", "key2": "val2"},
                ["key1"],
                {"key1": "val1"}
            )
        ]
    )
    def test_include_keys(self, test_name, input_dictionary: dict, input_keys: list, expected: dict):
        """
        Test include_keys method.

        Args:
            test_name (str): Test case name.
            input_dictionary (dict): Input Dictionary.
            input_keys (list): Input keys.
            expected (dict): Expected result.

        """
        actual = GeneralUtils.include_keys(input_dictionary, input_keys)
        self.assertEqual(expected, actual, test_name)

    @parameterized.expand(
        [
            (
                "Basic test",
                {"key1": "val1", "key2": "val2"},
                ["key1"],
                {"key2": "val2"}
            )
        ]
    )
    def test_exclude_keys(self, test_name, input_dictionary: dict, input_keys: list, expected: dict):
        """
        Test exclude_keys method.

        Args:
            test_name (str): Test case name.
            input_dictionary (dict): Input Dictionary.
            input_keys (list): Input keys.
            expected (dict): Expected result.

        """
        actual = GeneralUtils.exclude_keys(input_dictionary, input_keys)
        self.assertEqual(expected, actual, test_name)
