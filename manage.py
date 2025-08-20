#!/usr/bin/env python
# django command-line utility for administrative tasks
import os
import sys

def main():
    """
    entry point for django's command-line utility.
    sets the default settings module for the project,
    imports and runs the command execution function,
    and handles errors if django is not properly installed.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "couldn't import django. are you sure it's installed and "
            "available on your pythonpath environment variable? did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
