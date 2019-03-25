"""
Classes 2




"""

### Importing in Python

## Basics and built-in libraries

# importing a built in library - os will interact with the operating system
import os
x = os.environ
print(x)
print(x['NUMBER_OF_PROCESSORS'])


# if you're going to call os.environ a lot, you can use this syntax
from os import environ
x = environ  # no need to use "os." anymore, we have import environ directly
print(x['NUMBER_OF_PROCESSORS'])


# you can even rename them with "as"
from os import environ as env
x = env
print(x['NUMBER_OF_PROCESSORS'])


# os.listdir() is probably my most used function from os
files = os.listdir('data/')  # look inside a folder called 'data' that is in the same folder as this script
old_files = os.listdir(r"C:\Users\klevi\Desktop\box\bioinformatics\04_file_types\data")  # if a string is preceded by "r", it is a raw string that ignores all special characters like "\"
print(files)
print(old_files)


## Importing your own code

# None of these work!
# import FastaReader
# import practice_problems_9
# from practice_problems_9 import FastaReader
# from C:\Users\klevi\Desktop\box\bioinformatics\09_classes2\practice_problems_9 import FastaReader


## we have two options here,
#  1. add the location of fasta_reader to the list of paths that python looks for imports in
#  2. specify the path to that file relative to this file


## 1. Adding the location of fasta_reader to paths
#  but first, how do you check what paths are searched through?
import sys
print(sys.path)

# notice that the folder containing this script is (probably) the first element in sys.path
sys.path.append(r'C:\Users\klevi\Desktop\box\bioinformatics\09_classes2\practice_problems_9')
print(sys.path)  # look! we added it to the end, it was that easy!

# even though these statements have red underlines, they will work at run time, because sys.path was appended at run time
import practice_problems_9
from practice_problems_9 import FastaReader


## 2. Importing a file relative to this script's location


# python does not use "|" or "/" in imports, instead "." is used where,
#  each . at the beginning is equivalent to .. in unix (go to parent folder)
#  each . in the middle is equivalent to "/" or "\"

# from bioinformatics.lecture_10_exam2.real_exam2 import FastaReader
# To break down this example
#  from bioinformatics                                                   -    I have a folder in my sys.path called bioinformatics,
#                     .                                                  -    go inside of the folder,
#                      lecture_10_exam2                                  -    look for a folder called lecture_10_exam2,
#                                      .                                 -    go inside of that folder,
#                                       real_exam2                       -    look inside the file real_exam2,
#                                                  import FastaReader    -    for something called FastaReader
#                                                                        -    (FastaReader can be a def/class/variable)


## How do I permanently add something to PYTHONPATH?
# It depends on your operating system.
#   Windows users:
#   https://docs.python.org/3/using/windows.html#excursus-setting-environment-variables
#
#   Unix(MAC):
#   https://stackoverflow.com/questions/3402168/permanently-add-a-directory-to-pythonpath/21408970




###  Style

## "Main" method in python


if __name__ == '__main__':
    x = "Code inside of this IF statement will only run if this script itself is run - not when it is imported"
    assert len(x) > 5, "From now on, assert statements should go in the Main method, unless you want them to trigger when your code is imported"


## the argparse module (Running your program from a shell)
# Don't memorize this, just understand how it works and copy/paste
# You should almost always put this inside of  if __name__ == '__main__':
import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-i', '--input', help='Input', required=True)
    parser.add_argument('-o', '--output', help='Output')
    parser.add_argument('-n', help='Some Number', type=int)
    parser.add_argument('-v', help='Verbose', action='store_true')

    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        sys.exit(1)

    if not args.n:
        args.n = 10  # set the default to 10 if not specified by user

    if not args.output:
        args.output = sys.stdout  # this little trick is clever,
        # from here on, all code that would write to the file args.output
        # both outfile.write() and sys.stdout.write() use methods of the same name



## Order of a generic Python script
# 0. Beginning Docstring/Version
# 1. Imports
# 2. Classes
# 3. Defs
# 4. if __name__ == '__main__':
# 5. argparse (optional)
# 6. <do something with arguments>



## For an example, please see Practice_Problems_9





