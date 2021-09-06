# Repo name: puneetha-python-template

<!--BEGIN-->
---

# Summary

Python template - Project structure.

---
<!--END-->
 

<!--BEGIN-->
---

# Good practices

1. With the evolution of Cloud; you are not restricted to using/managing config file/s, you can also rely on Cloud
   services like AWS Secrets Manager, SSM Parameter Store, etc. to maintain secret values or even default values
2. Never ever Hard code environment name, even if you have just 1 environment. It has to either come from environment
   variable or config file or some other mechanism
3. Prefix your environment variables with something specific to your project, to avoid conflicts with other projects.
   For this package, I choose "PBM_"
4. Keep your environment variable mapping in 1 common place. Use the python variables to map it to minimize the impact
   of change
    - Ex: puneetha-python-template/utils/constants/env_variable_mapper.py
5. Always use a code linter of your choice from day 1 of your project
6. Stick to 1 convention - choose between Singular vs Plural! Ideally Singular!

---
<!--END-->

<!--BEGIN-->
---

# Python main packages used

1. **mypy** - Type checking
2. **pytest** - Testing python package
3. **pylint** - Codestyle checker
4. **pydocstyle** - Docstring style checker
5. **pdoc3** - Docstring generator python package
6. **loguru** - Logging
7. **tox** - Running test suite
8. **mkdocstrings** - Static site generator from "*.md" files

---
<!--END-->

<!--BEGIN-->
---

# Set-up instructions [here](./project_docs/DEV_SETUP.md)

---
<!--END-->


<!--BEGIN-->
---

# Build process [here](./project_docs/BUILD_PROCESS.md)

---
<!--END-->

<!--BEGIN -->
---

# You are all set to Fly! :)

---
<!--END-->
