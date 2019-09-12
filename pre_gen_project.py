from pathlib import Path
print("hello world")


import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

nb_name = '{{ cookiecutter.nb_name_processing }}'

if not re.match(MODULE_REGEX, nb_name):
    print('ERROR: %s is not a valid Python module name!' % nb_name)

    # exits with status 1 to indicate failure
    sys.exit(1)