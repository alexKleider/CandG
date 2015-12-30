#!../venv/bin/python
"""  File: assessingOS.py
ASSESSING THE OPERATING SYSTEM
Obtaining Information About Users and Their Computer
Learn usage of the following library functions:
    sys.getfilesystemencoding()
    os.getlogin()
    os.getuid()
    pwd.getpwuid()  | Both return the same object which
    pwd.getpwnam()  | has an attribute for each component.
    pwd.getpwall()
"""
import os
import sys
import pwd   # A window into /etc/passwd file.
import locale

sys_encoding = sys.getfilesystemencoding()
print("File system encoding (from sys module) is '{}'."
            .format(sys_encoding))
locale_encoding= locale.getpreferredencoding()
print("Preferred encoding (from locale module) is '{}'."
            .format(locale_encoding))
if locale_encoding.upper() == sys_encoding.upper():
    print("They are both the same.\n")

print("User Info:")
user = os.getlogin()
uid = os.getuid()
print("\tCurrent user: {}".format(user))
print("\tCurrent uid: {}".format(uid))

pw_by_uid =  pwd.getpwuid(os.getuid())
print("\nEntry in /etc/passwd retrieved by user ID:")
print(pw_by_uid)

pw_by_name = pwd.getpwnam(user)
print('\nEntry retrieved by user name is of type {},'
                            .format(type(pw_by_name)))
if pw_by_uid == pw_by_uid:
    print('and is the same as that retrieved by user ID.')
#print('...and is displayed as:')
#print(pw_by_name)
print(
"\nIt (however obtained,) can be displayed with a for loop:")
print('; '.join([str(entry) for entry in pw_by_name]))
#for entry in pw_by_name:
#    print("\t{}".format(entry) )
print("\n...or individually using attributes:")
print('; '.join([   pw_by_name.pw_name,
                    pw_by_name.pw_passwd,
                    str(pw_by_name.pw_uid),
                    str(pw_by_name.pw_gid),
                    pw_by_name.pw_gecos,
                    pw_by_name.pw_dir,
                    pw_by_name.pw_shell    ]))
print("\n...or using indeces as we'll see below.")
pw_all = pwd.getpwall()
print("""
One can also obtain a complete list representing all entries in the
/etc/passwd file.  We'll display only the user name for each entry:""")
print(', '.join([id[0] for id in pw_all]))
print("""
Just don't forget that the IDs are integers and must be converted
to strings if/when they are part of a list that is to be used as a
parameter for the join() function.""")
