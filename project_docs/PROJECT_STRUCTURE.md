# Python Project Structure

<!--BEGIN-->
---
```
puneetha_python_template -> Python template files
├── __init__.py -> initializes the application, indicated that this folder is a python module
├── ... -> Python files
├── utils -> Helper utilities/functions which can be used across projects
|   ├── __init__.py -> initializes the application, indicated that this folder is a python module
|   ├── file_utils.py -> File Utilities
|   └── constants - Project specific constants
|       ├── __init__.py
|       └── ... -> Default values python files
|
└── tests -> Unit test files
|       ├── __init__.py
|       └── test_file_utils.py
|       └── test_constants - Project specific constants
|           ├── __init__.py
|           └── ... -> Default values python test files
|
├── integration_tests -> Integration test files
│   ├── __init__.py
|   └── ... -> Test files
|
├── config -> Configuration files for code style, etc.
│   ├── .pylintrc -> Enforce PEP8 Code Style
│   ├── .pydocstylerc -> Enforce docstring style
│   ├── mkdocs.yml -> Enforce md file generator instructions
│   ├── .mypy.ini -> Type checking options
│   └── tox.ini -> Pytest config - test a python package in a set of virtual environments
|
├── requirements.txt -> This file lists all of the Python packages that your app depends on
|
├── setup.py -> Python dependency management tool
|
├── README.md -> Summary of the project and any helpful documentation
|
├── .gitignore -> Instructs git to ignore the files/directories specified in this file
|
├── .pre-commit-config.yaml -> Managing and maintaining pre-commit hooks
|
├── scripts -> General scripts, deployment scripts, etc.
|
├── project_docs -> detailed set of readme files for developers
|   ├── images -> Images to be used in readme documents
|       └── ... -> All images which helps in documentation
|   ├── PROJECT_STRUCTURE.md -> Project Structure
|   ├── DEV_SETUP.md -> Developer Setup Guidelines
|   └── ... -> All helpful documentation which might help developers
|
├── docs -> Devops related documents
├── └── pull_request_template  -> pull request templates
|       ├── pull_request_template.md -> Default pull request template. Default: feature branch
|       └── branches -> Branch specific pull request templates
|           ├── feature.md -> Feature branch pull request template
|           ├── release.md -> Release branch pull request template
|           ├── bugfix.md -> Bugfix branch pull request template
|           └── hotfix.md -> Hotfix branch pull request template
|      
├── dist -> Generated egg files -> Not committed to git
|
├── scratch -> Random adhoc stuff - Not committed to git
|
├── auto_generated -> Auto Generate documents - Not committed to git
├── ├── docstrings  -> Docstrings -> Not committed to git
└── └── test_coverage -> Test coverage report -> Not committed to git
```

---
<!--END-->