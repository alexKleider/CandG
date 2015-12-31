#!../venv/bin/python
"""  File: wcdm.py  (wildcards, copying, deleting, moving files)
Navigating and Manipulating the File system
-------------------------------------------

Built-in functions for opening, reading and writing files
os.module: functions to manipulate files as complete entities-
    renaming, deleting, creating links.
shutil.module (and other utility modules) work along side os.module.
NOTE: pathlib.module in 3.4 is provisional (and therefore not covered.)

os.listdir()    #|  Previously
os.getcwd()     #|   covered.
os.mkdir()
os.makedirs()
os.chdir()
os.remove()
os.rmdir()    # Same as rm <dir_name>: directory must be empty.
shutil.copy()
shutil.copytree()
shutil.move()
shutil.rmtree()  # Equivalent to rm -r <dir_name>
glob.glob()      # Same as os.listdir() but recognizes glob characters.
"""

import os
import shutil as sh
import glob

dir_names = []
file_names = ['fileA.txt', 'fileB.txt', 'ls.txt']

def setup(dir_names, file_names):
    print("Setting up the following: {}\n"
                .format(file_names + dir_names))
    for dir_name in dir_names:
        os.makedirs(dir_name)
    for file_name in file_names:
        with open(file_name, 'w') as file_object:
            file_object.write("#   File: {}"
                    .format(file_name))

def teardown(dir_names, file_names):
    print("\nClean up: removing the following: {}"
                .format(file_names + dir_names))
    for dir_name in dir_names:
        sh.rmtree(dir_name)
    for file_name in file_names:
        os.remove(file_name)

setup(dir_names, file_names)

cwd = os.getcwd()
print("""After <setup> 'cwd = os.getcwd()', cwd ==> {}"""
                    .format(cwd))
listing1 = os.listdir(cwd)
print("""'listing1 = os.listdir(cwd)', 'listing1' ==> {}"""
                .format(listing1))
os.mkdir("subdir")
listing2 = os.listdir(cwd)
dir_names.append("subdir")
print(
"""After 'os.mkdir("subdir")' &
'listing2 = os.listdir(cwd)':
'listing2' ==> {}""".format(listing2))
if (set(listing1) | set(["subdir"])) == set(listing2):
    print("Listings are as they should be. All is well.")
else:
    print("Listings are not what they should be!")
os.chdir("subdir")
print("""
After 'os.chdir("subdir")', 'os.getcwd()' ==> {}"""
            .format(os.getcwd()))
os.chdir("..")
print("""After 'os.chdir("..")', 'os.getcwd()' ==> {}"""
            .format(os.getcwd()))
try:
    os.mkdir("test2/newtestdir")
except OSError:
    print(
"""'os.mkdir("test2/newtestdir")' failed because of an OSError""")
os.makedirs("test2/newtestdir")
print("""'os.makedirs("test2/newtestdir")' however succeeds.""")
os.chdir("test2/newtestdir")
print(
"""After 'os.chdir("test2/newtestdir")', 'os.getcwd()' ==>
            {}"""
            .format(os.getcwd()))
os.chdir(cwd)
with open("test.py", 'w') as file_object:
    file_object.write("#    File: ".format("test.py"))
file_names.append("test.py")
if os.listdir(".") == glob.glob("*"):
    print("""'os.listdir(".")' == 'glob.glob("*")'""")
else:
    print(
    """'os.listdir(".")' and 'glob.glob("*")' ARE NOT THE SAME""")
print("""Other suggested commands follow:
glob.glob("")
glob.glob("")
glob.glob("")
glob.glob("")
glob.glob("")""")

sh.copy("fileA.txt", "fileX.txt")
sh.copy("fileB.txt", "subdir/fileY.txt")
print("""After 'sh.copy("fileA.txt", "fileX.txt")'
and 'sh.copy("fileB.txt", "subdir/fileY.txt")',""")
if (  ("fileX.txt" in os.listdir("."))
and ("fileY.txt" in os.listdir("subdir"))  ):
    print(
"""'fileX.txt' and 'subdir/fileY.txt' have been created.""")
else:
    print("SOMETHING IS NOT RIGHT[1]!!")
    print("""'fileX.txt' should be in {}"""
                .format(os.listdir(".")))
    print("""and 'fileY.txt' should be in {}"""
                .format(os.listdir("subdir")))
sh.copytree("subdir", "test3")
print("""After 'sh.copytree("subdir", "test3")'""")
if os.listdir("subdir") == os.listdir("test3"):
    print(
"""'os.listdir("subdir") == os.listdir("test3")' ==> True""")
else:
    print("SOMETHING IS NOT RIGHT[2]!!")
sh.rmtree("test2")

os.mkdir("test4")
sh.move("subdir/fileY.txt", "test4")
print("""After 'os.mkdir("test4")' and
'sh.move("subdir/fileY.txt", "test4")'
'os.listdir("subdir")' ==> {}
and 'os.listdir("test4")' ==> {}"""
        .format(os.listdir("subdir"), os.listdir("test4")))
os.remove("test4/fileY.txt")
print("""...then after 'os.remove("test4/fileY.txt")'
'os.listdir("test4")' ==> {}"""
        .format(os.listdir("test4")))
try:
    os.remove("test4")
except OSError:
    print("""'os.remove("test4")' raises an 'OSError'!
because 'os.remove()' works on files, not directories.""")
else:
    print("""AN ERROR SHOULD HAVE BEEN RAISED[3]""")
print("""For directories, the command is 'sh.rmtree("test4")'""")
sh.rmtree("test4")
print(
"""Also running 'sh.rmtree("test3")' & 'os.remove("fileX.txt")'.""")
sh.rmtree("test3")
os.remove("fileX.txt")

teardown(dir_names, file_names)
