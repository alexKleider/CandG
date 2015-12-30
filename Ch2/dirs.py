#!../venv/bin/python
"""   File: dirs.py
Navigating and Manipulating the File System
-------------------------------------------
Accesssing Directories in Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import os

cwd = os.getcwd()
print("os.getcwd() ==> '{}'.".format(cwd))
print("\nos.listdir(os.getcwd()) ==>")
print(os.listdir(cwd))
os.mkdir("subdir")
print("""\nSame command after 'os.mkdir("subdir")' ==>""")
print(os.listdir(cwd))
os.chdir("subdir")
print("""\nAfter 'os.chdir("subdir")', 'os.getcwd()' ==> {}"""
            .format(os.getcwd()))
os.chdir("..")
print("""\nAfter 'os.chdir("..")', 'od.getcwd()' ==> {}"""
            .format(os.getcwd()))
try: 
    os.mkdir("test2/newtestdir")
    print("Unexpected successful 'os.mkdir'!!")
except OSError:
    print("""
os.mkdir("test2/newtestdir") fails  but
os.makedirs("test2/newtestdir") creates intermediary directories.""")
    os.makedirs('test2/newtestdir')
cwd1 = os.getcwd()
assert cwd == cwd1
print('Current working directory is {}.'.format(cwd1))
print('Listing {}:'.format(cwd1))
print(os.listdir(cwd1))
print("Listing 'test2': {}"
            .format(os.listdir('test2')))
os.chdir("test2/newtestdir")
print("""After 'os.chdir("test2/newtestdir"), 'os.getcwd()' ==>""")
print(os.getcwd())

# Clean up:
os.chdir(cwd)
os.rmdir('subdir')
os.rmdir('test2/newtestdir')
os.rmdir('test2')
