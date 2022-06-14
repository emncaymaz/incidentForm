# incidentform
Django based project for "Sicherheitsvorfälle melden" used to manage companies.

# Installation

# Create a python3 virtualenv:
python3 -m venv venv

# activation virtualenv

source venv/bin/activate
# Install all dev-dependencies for the project:

pip install -r requirements-dev.txt
python manage.py migrate

# Management Command run commands are below.
python manage.py cleanup_forms



