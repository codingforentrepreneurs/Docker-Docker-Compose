#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import dotenv
import sys
import pathlib
# django-dotenv

def main():
    USE_DOTENV = os.environ.get("USE_DOTENV_PKG")
    if str(USE_DOTENV) == "1":
        base_path = pathlib.Path(__file__).resolve().parent
        dotenv.read_dotenv(base_path / ".env-dev")
        print('REDIS_PORT', os.environ.get('REDIS_PORT'))

    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cfehome.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
