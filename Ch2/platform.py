#!../venv/bin/python
"""
    File: platform.py
Explores:
    sys.platform
    os.name
    os.uname  | Returns a data structure similar to pwd.struct_passwd.
    shutil.get_terminal_size()
"""

import os
import sys
import shutil

print("sys.platform is '{}'.".format(sys.platform))
print("os.name is '{}'.".format(os.name))
print("os.uname() yields the following:\n{}".format(os.uname()))
print("""
Note the similarity between the way the last item is reported
and the way 'pwd.struct_passwd' was reported in assessingOS.py.""")

cols, lines = shutil.get_terminal_size()
print("The terminal window is {} wide with {} lines."
        .format(cols, lines))
