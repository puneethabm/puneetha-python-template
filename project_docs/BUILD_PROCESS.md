<!--BEGIN-->
---

# Build process

1. Install all the packages listed in requirements.txt file
    ```shell
    pip install -r requirements.txt
    ```

2. Docstring style checker
    ```shell
    # Simple
    pydocstyle <package_name>
    
    # Config
    pydocstyle --config=config/.pydocstylerc <package_name>
    
    # Run pydocstyle for specific folder:
    # Ex: run pydocstyle for folder 'puneetha_python_template/utils'
    PYDOCSTYLE_FILES=$(find puneetha_python_template/utils -type f -name "*.py")
    echo PYDOCSTYLE_FILES
    pydocstyle --config=config/.pydocstylerc $PYDOCSTYLE_FILES
    
    ```

3. Codestyle checker
    ```shell
    # Simple test without config
    pylint <package_name>
    
    # Custom config
    pylint --load-plugins pylint_quotes --rcfile=config/.pylintrc <package_name>
    
    # Add processes
    pylint --verbose -j 2 --load-plugins pylint_quotes --rcfile=config/.pylintrc <package_name>
    
    # Run pylint for specific folder - display errors only:
    # Ex: run pylint for folder 'puneetha_python_template/utils'
    PYLINT_FILES=$(find puneetha_python_template/utils -type f -name "*.py")
    echo $PYLINT_FILES
    pylint -E --load-plugins pylint_quotes --rcfile=config/.pylintrc $PYLINT_FILES
    
    ```

4. Run tests
   ## Run test from config file:
    ```shell
    pytest -c ./config/tox.ini
    ```

   ## Run test from arguments
    ```shell
    pytest -c ./config/tox.ini --cov-report html:auto_generated/coverage --cov=usage
    ```

   ## Run test for specific subpackage folder
    ```shell
    pytest --cache-clear -p no:warnings  -rp --html=auto_generated/pytest_report.html --cov-report html:auto_generated/html_cov --ignore=puneetha_python_template/utils/custom_logger.py puneetha_python_template/utils
    ``` 

   ## Run unittest from command line. Example:
    ```shell
    python -m unittest puneetha_python_template.tests.test_utils.test_general_utils.TestGeneralUtils
    ```
    (or)
    ```shell
    python -m unittest puneetha_python_template/tests/test_utils/test_general_utils.py
    ```

5. Generate docstring & publish
   ## Launch the docstring
    ```shell
    pdoc3 puneetha_python_template --http :8099
    ```

   ## Save the docstring to a html file
    ```shell
    pdoc3 puneetha_python_template --force --html -o auto_generated/docstrings
    ```
6. Generate mkdocs
   # How to make MkDOcs
   ### Configuration: https://www.mkdocs.org/user-guide/configuration/
   ### Example: https://docs.civicrm.org/dev/en/latest/extensions/documentation/
   
   ```shell
   # Start server:
   mkdocs serve --config-file ./config/mkdocs.yml
   # Output: Serving on http://127.0.0.1:8000/
   ```
   
   ### Deploy: https://www.mkdocs.org/user-guide/deploying-your-docs/
   ```shell
   mkdocs gh-deploy --clean --config-file  ./config/mkdocs.yml
   ```
   
7. Build egg file
    ```shell
    python setup.py bdist_egg
   
    # (or) with install
    python setup.py install bdist_egg
    ```

8. Loguru read more [here](https://readthedocs.org/projects/loguru/downloads/pdf/latest/)

---
<!--END-->