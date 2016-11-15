#!/usr/bin/env python

import os
import sys

from django.core.management import execute_from_command_line


BASEDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, BASEDIR)

os.environ["DJANGO_SETTINGS_MODULE"] = "testproject.settings"

if __name__ == "__main__":
    execute_from_command_line(sys.argv)
