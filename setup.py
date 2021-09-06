"""
Set up.

@author: Puneetha Bagivalu Manjegowda
"""

import os

from setuptools import find_packages, setup

try:
    # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    # for pip <= 9.0.3
    from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement objects
INSTALL_REQS = parse_requirements("requirements.txt", session="hack")

try:
    REQS = [str(ir.req) for ir in INSTALL_REQS]
except AttributeError:
    REQS = [str(ir.requirement) for ir in INSTALL_REQS]

VERSION = "1.0.0"

setup(name="puneetha-python-template",
      version=VERSION,
      author="Puneetha Bagivalu Manjegowda",
      author_email="puneethabm@gmail.com",
      description="Python template Package!",
      long_description=open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "./project_docs/index.md")).read(),
      include_package_data=False,
      zip_safe=False,
      keywords="python template",
      install_requires=REQS,
      packages=find_packages(exclude="tests"),
      setup_requires=[],
      tests_require=["pytest", "pytest-runner", "pytest-pylint", "coverage"],
      py_modules=[],
      classifiers=["Programming Language :: Python :: 3.7"],
      python_requires=">=3.7")
