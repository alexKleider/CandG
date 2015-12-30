#!../venv/bin/python
import os

proc_id = os.getpid()
parent_id = os.getppid()
env_dict = os.environ
print("Current process ID is {},".format(proc_id))
print("& its parent process ID is {}.".format(parent_id))
print("The number of set environment variables is {}."
                .format(len(env_dict)))
bogus = input("Provide a bogus environment variable: ")
print("""Anything you provided will work because it comes in as a string
but remember that only strings can be assigned to an environmental
variable.
""")
os.environ['BOGUS'] = bogus
print("""
Some selected environment variables:""")
for env_var in ('BOGUS',
                'HOME',
                'USER',
                'LOGNAME',
                'TERM',
                'PYTHONPATH',
                'PWD',
                'work',
                'OLDPWD',
                'EDITOR',
                'LANGUAGE',
                'LANG',
                'SHELL',
                'OS',
                'PROCESSOR_ARCHITECTURE'):
    try:
        print("\t{}: {}".format(env_var, env_dict[env_var]))
    except KeyError:
        print("\t{} is NOT set.".format(env_var))
del(os.environ['BOGUS'])

print('Now you can see them all...')
counter = 10
for key in env_dict:
    if counter == 10:
        counter = 0
        _ =  input("[<---'] (Enter) TO CONTINUE, CTRL-C TO QUIT: ")
    print("{}: {}".format(key, env_dict[key]))
    counter += 1

