"""General utilities package."""

from puneetha_python_template.utils.custom_logger import CustomLogger


class GeneralUtils(CustomLogger):
    """General utilities."""

    def __init__(self):
        """General utilities."""
        CustomLogger.__init__(self, __name__)
        self.logger.debug("General utilities Constructor")

    @staticmethod
    def include_keys(dictionary: dict, keys: list) -> dict:
        """
        Filter a dict by only including certain keys.

        Args:
            dictionary (dict): Dictionary.
            keys (list): Keys.

        Returns:
            dict: Dictionary.

        """
        key_set = set(keys) & set(dictionary.keys())
        return {key: dictionary[key] for key in key_set}

    @staticmethod
    def exclude_keys(dictionary: dict, keys: list) -> dict:
        """
        Filter a dict by excluding certain keys.

        Args:
            dictionary (dict):
            keys (list): Keys.

        Returns:
            dict: Dictionary.

        """
        key_set = set(dictionary.keys()) - set(keys)
        return {key: dictionary[key] for key in key_set}
