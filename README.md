# Introduction

A repository of tools to build a fully functioning backend. Built by canibalizing the best parts of all previous projects.

# Features

A fully functioning backend with API endpoints which:

- Performs CRUD methods on a given SQL database
- Presents options to search, paginate, and sort database fields
- User authentication and hashing modules

And also:

- A working docker and docker-compose file
- Pre-commit hooks: Black formatter + isort + conventional commits

# First steps

1. Install [poetry](https://python-poetry.org/docs/1.3#installing-with-the-official-installer)
2. Delete the `poetry.lock` and `pyproject.toml` files respectively
3. Run `poetry init` to initialize a fresh virtual environment
4. Install recommended packages

# Recommended packages

```
#################################
# Note: You can just copy and paste
# this entire code block in your terminal
# without repercussions
#################################


#################################
# Compulsory
#################################
poetry add requests &&
poetry add "uvicorn[standard]" &&
poetry add fastapi &&

#################################
# Good to have settings
#################################
poetry add -D black &&
poetry add -D loguru &&

#################################
# Precommit setup
#################################
poetry add -D pre-commit &&
poetry shell &&
pre-commit install
pre-commit install --hook-type commit-msg


#################################
# Project dependent dependencies
#################################
poetry add sqlalchemy &&                # For SQL databases
poetry add \
"python-jose[cryptography]" &&          # For creating JWT tokens
poetry add "passlib[bcrypt]"            # For hashing/unhashing passwords

```

# Recommended settings

Create a .env file and initialise an IS_DEV constant. This IS_DEV boolean would be used switch between dev and production settings (secrets/swagger UI etc.)

Ensure that the .env file is not committed to this repository or your docker files by adding it to your .gitignore and .dockerignore files respectively. 

# File setup

- You don't have to use all the modules (obviously). Feel free to delete modules you do not use
- Constants defined at the top of a module should typically be moved to the constants.py folder (unless there is a compelling reason not to)

# Commit messages

{type}{optional scope}: {description}

{optional footer prepend}: {footer}

types

- fix: Bug fixes
- feat: New feature
- refactor: Code changes that neither fixes bugs nor adds features
- perf: Performance improvement
- docs: Documentation change
- ci: Changes to CI configs
- build: Changes that affect the build system or external dependencies

footer prepend

- BREAKING CHANGE

Features of a good description

- Imperative mood
- Concise
- Direct
- Addresses the following:
  - Why did you make the change? What was the effect? What were the changes in reference to?

{description} = {did thing} + {impacted thing} + {greater purpose}
{description} = {achieved greater purpose} + {did thing}

# Task list

Canibalise all previous projects to obtain the following:

- [x] Code snippets to query SQL DBs
- [ ] Code snippets to query from noSQL DBs
- [ ] Code snippets to query from noSQL DBs
- [x] Yaml config file for pre-commit hooks
- [x] Docker and docker-compose.yml templates
- [x] FastAPI router setup
- [x] Code snippets for Authentication
- [ ] Telegram bot template
- [ ] Deployment automation tools
- [ ] Do one for the frontend too (separate repo)

During this process, I should also canibalise the methods of abstraction. I should:

- [ ] For code snippets, write inline comments on on WHY certain code snippets are written the way they are
- [ ] For repo structures, write README.md files on WHY the a directory is needed for its component modules

Finally, I should

- [ ] Note down things that I should replace/destory when using this repo as a template for a project
- [ ] Note down the contents of this repository for easy navigation, and easy canibalisation [meta-canibalisation lol]
