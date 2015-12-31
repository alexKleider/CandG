#!../venv/bin/python
"""    File: util.py   # Further discussion of shutil  methods.
Continuation of "Using Wildcards, Copying, Deleting, Moving Files."

Features included in shutil module:
    * Creation of zip or tar archived or compressed files.
    * Extended functionality using optional args:
        eg: shutil.copytree(ignore=<func(root_folder, list_of_files)>)
        'ignore' can be set to the helper function
            shutil.ignore_patterns()
"""


