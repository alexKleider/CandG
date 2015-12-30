#!../venv/bin/python
"""    File: info.py
Obtaining Information About Files (and Devices)
-----------------------------------------------
File Status and Permissions:

    os.listdir()
    os.stat()
    os.access()
    time.localtime()
    time.strftime()
"""
import os
import time
import shutil as sh

dir_names = []
file_names = []

def setup(dir_names, file_names):
    for dir_name in dir_names:
        pass
    for file_name in file_names:
        pass

def teardown(dir_names, file_names):
    for dir_name in dir_names:
        pass
    for file_name in file_names:
        pass

print("""'os.listdir(".")' ==> {}""".format(os.listdir(".")))
stats = os.stat("README")
print("""'os.stat("README")' ==> {}""".format(os.stat('README')))
mtime = stats.st_mtime
print("""'os.stat("README").mtime' ==> {}"""
                .format(os.stat("README").st_mtime))
print("""...which we'll assign to 'mtime' and then...
'time.localtime(mtime)' (a time tuple): ==> {}"""
                .format(time.localtime(mtime)))
print("""...a friendlier version of which would be...
'time.strftime("%Y-%m-%d %H:%M", time.localtime(mtime))' ==> {}"""
    .format(time.strftime("%Y-%m-%d %H:%M", time.localtime(mtime))))
mode = stats.st_mode
print("""
We've assigned 'os.stat("README")' to 'stats' and
having looked at stat.st_mtime, now let's check out st_mode.
'stats.st_mode' ==> h/{:x} d/{:d} o/{:o} b/{:b}
The parts that interest us are the last 9 bits: o/{} or b/{} {} {}."""
        .format(mode, mode, mode, mode,
                "{:o}".format(mode)[-3:],
                "{:b}".format(mode)[-9:-6],
                "{:b}".format(mode)[-6:-3],
                "{:b}".format(mode)[-3:]))
print(
"""Convenience functions provide access to the same information:
'os.access('README', os.F_OK)' (for 'file exists') ==> {}
'os.access('README', os.R_OK)' ('read') ==> {}
'os.access('README', os.W_OK)' ('write') ==> {}
'os.access('README', os.X_OK)' ('Execute') ==> {}""".format(
os.access('README', os.F_OK),
os.access('README', os.R_OK),
os.access('README', os.W_OK),
os.access('README', os.X_OK)))
print("""
The above not withstanding: remember that the Pythonic way is
to ask forgiveness afterwards rather than permission before:
    try:
        myfile = open(<filename>)
    except PermissionError:
        pass # test/modify permissions
    else:
        pass # process file
    finally:
        pass # close file""")


