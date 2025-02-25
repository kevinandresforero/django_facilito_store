#!/bin/bash

# Create a VEnv for Python 3.13.2
pyenv install 3.13.2
pyenv virtualenv 3.13.2 web-django
pyenv activate web-django

# Install General Dependencies
pip install --upgrade pip
pip install ipython
pip install poetry
poetry config virtualenvs.in-project true
poetry --version


# create poetry project and add dependencies
poetry new django-poetry
cd django-poetry

poetry add numpy pandas beautifulsoup4 matplotlib seaborn psycopg2>
poetry add -G dev black pylint pytest click pre-commit
pip install ydata-profiling


# Restart shell
