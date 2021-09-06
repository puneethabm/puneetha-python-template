"""File utilities."""

import os
import sys
from typing import Tuple

from puneetha_python_template.utils.constants.env_variable_mapper import EnvironmentVariableMapper
from puneetha_python_template.utils.custom_logger import CustomLogger


class FileUtils(CustomLogger):
    """File utilities."""

    def __init__(self):
        """Instantiate File utilities."""
        CustomLogger.__init__(self, __name__)

    def get_project_path(self, module_name: str = EnvironmentVariableMapper.PBM_MODULE_NAME.value) -> str:
        """
        Get project path.

        Args:
            module_name (str): Module name.

        Returns:
            str: Root directory name.

        """
        root_dir: str = os.path.dirname(sys.modules[module_name].__file__)
        self.logger.debug(f"root_dir: {root_dir}")
        return root_dir

    def get_python_file_project_relative_path(self, python_file_name: str) -> str:
        """
        Get Python file project relative path.

        Args:
            python_file_name (str): Python file name.

        Returns:
            str: Project relative path of the python file.

        """
        project_path_list: Tuple[str, str] = os.path.split(self.get_project_path())
        relative_path: str = python_file_name.__file__

        relative_path = relative_path.replace(project_path_list[0], "")
        self.logger.debug(f"relative_path: {relative_path}")
        return relative_path
