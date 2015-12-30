#!../../venv/bin/python3
"""    File: grepword.py
Takes a word and one or more file names as commandline parameters
and returns a list of file name, line number and line when ever the word
is encountered in the line.
"""
import sys

if len(sys.argv) < 3:
    print("Must provide a word and at least one file name.")
    sys.exit()

word = sys.argv[1]
for file_name in sys.argv[2:]:
    for lino, line in enumerate(open(file_name)):
        if word in line:
            print("{} #{}: {:.40}"
                    .format(file_name, lino, line.rstrip()))

