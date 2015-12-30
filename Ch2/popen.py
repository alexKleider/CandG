#!../venv/bin/python
"""    File: popen.py
**Managing Subprocesses More Effectively**
The subprocess.Popen class can be used to create an instance of a
process or command.
Our python script can then accept its output or send to its input
(receiving/sending byte strings) by redirecting stdout/stdin to sub.PIPE
and then reading its stdout attribute or using the write method of its
stdin attribute.  Note: When referring to stdin or stdout, distinguish
its use as a parameter from when it refers to an attribute.
"""

import os
import sys
import subprocess as sub

def print_dot_files():
    print("""
    This function prints a listing of all *.* files in the cwd.
    To capture its output we set stdout=sub.PIPE and refer to its
    stdout attribute which has a read() method or can be treated as
    an iterable in the same way that we deal with files:""")
    ls = sub.Popen(['ls', '*.*'], shell=True, stdout=sub.PIPE)
#   print(ls.stdout.read())
    print(ls.stdout.read().decode('utf-8'), end= '')
#   for l in ls.stdout:
#       print(l.decode('UTF-8')[:-1])
    print("Note also: once read, further reads, yield nothing.")

def remove(file_name):
    os.remove(file_name)
    try:
#       os.remove(file_name)
        sub.call(['rm', file_name])
    except FileNotFoundError:
        print("!!!File {} not found!!!".format(file_name))
    else:
        print("Successfully removed '{}'.".format(file_name))

os.chdir('root4subpro')
print("""
Working directory changed to {}."""
            .format(os.getcwd()))
print("""
Setting up an 'ls.txt' file as we did before.""")
assert sub.call(['ls'], stdout=open('ls.txt', 'w')) == 0
print("And check that it's there:")
assert sub.call(['ls']) == 0

print_dot_files()

print("""
For input we set stdin=sub.PIPE and use the write method of its
stdin attribute:""")
#ex = sub.Popen(['ex', 'test.txt'], shell=True, stdin=sub.PIPE)
ex = sub.Popen(['ex', 'test.txt'], stdin=sub.PIPE)

print(ex.stdin.write(b'i\nthis is a test\n.\n'))
print(ex.stdin.write(b'wq\n'))
try:
    failed = sub.Popen(["NonExixtentCommand"])
#except OSError:
except FileNotFoundError:
    print("""
Trying to run a non existent command results in 'FileNotFoundError' 
which we'll catch in a try/except statement.
""")
print_dot_files()
print("""
The files ls.txt and text.txt have been created and need removing.""")
remove('ls.txt')
remove('test.txt')
sys.exit()
print("Didn't work, perhaps because 'text.txt' is still in a buffer.")
del(ex)
#sub.call(['sync'])
print("""Try again after "del(ex)" or "sub.call(['sync'])""")
remove('test.txt')
print("SUCCESS!")


