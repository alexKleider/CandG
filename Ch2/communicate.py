#!../venv/bin/python
"""   File: communicate.py
An attempt to understand subprocess.Popen().communicate()
"""

import os
import subprocess as sub

print("Using subprocess.Popen.communicate----")
print("First call 'ex' to create 'myfile.txt' again:")
ex = sub.Popen(['ex', 'myfile.txt'], stdin=sub.PIPE,
                                    stdout=sub.PIPE)
ex_out, ex_err = ex.communicate(b'i\nthis is a test\n.\nwq\n')
print("Stdout: {}".format(ex_out))
print("Stderr: {}".format(ex_err))

print("""
Then use the example provided in the book to provide a listing
to demonstrate the presence of the new file:""")
ls = sub.Popen(['ls'], stdout=sub.PIPE)
listing = ls.communicate()[0]
print(listing)
print("Now there remains only to delete the file created by 'ex'.")

os.remove("myfile.txt")
