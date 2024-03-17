from lib import *
from os import listdir
from os.path import isdir
from subprocess import call

dirs = listdir()
dirs = [dir for dir in dirs if isdir(dir) and dir[0].isalpha()]

for dir in dirs:
    call(f"python {dir}/file.py")