#!../venv/bin/python
"""    File: subpro_call.py
**Managing Other Programs**
[
This section is contingent on presence of a directory
    Root4subpro (called 'root' in the text,)
containing two text files: fileA and fileB.
]
The shell command 'cd' seems not to be recognized.
Perhaps because it is a shell builtin command?
What ever the reason, os.chdir is being used in its stead.

We begin by using 
    subprocess.call()
It is a 'convenience function' provided by the subprocess module.
"Run command with arguments. Wait for command to complete, then return
the returncode attribute. Arguments are the same as for the Popen
constructor.  It will deadlock if the child process generates enough
output to a stdout or stderr pipe such that it blocks waiting for the OS
pipe buffer to accept more data.
It allows execution of a command (although not apparently of
a builtin) but does not allow interaction with the resulting process.  
It is however possible to write to a file which could then be read
(although doing so is a security risk and such files should be
deleted immediately after use, which we do with os.remove)

**Managing Subprocesses More Effectively**
The subprocess.Popen class can be used to create an instance of a
process or command.  This is covered in popen.py
"""

import os
import subprocess as sub

def list_cwd():
    print("Listing (ls -l) of current working directory:")
    assert sub.call(['ls', '-l']) == 0

list_cwd()
os.chdir('Root4subpro')
print("""
Working directory changed to {}."""
            .format(os.getcwd()))
list_cwd()

print("""
We'll now send the listing to a file and read it (using 'more').""")
assert sub.call(['ls'], stdout=open('ls.txt', 'w')) == 0
assert sub.call(['more', 'ls.txt']) == 0
print("""
Another listing follows, this time using shell expansion-
    ls *.t*xt
but for this to work, we must set shell=True, which is a potential
security risk.  We end by removing the ls.txt file.""")
assert sub.call(['ls', '*.t*xt'], shell=True) == 0
os.remove('ls.txt')


