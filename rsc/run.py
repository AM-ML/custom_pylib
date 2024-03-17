from os import listdir, chdir,getcwd
from os.path import isdir
from subprocess import call
from lib import plcyan,LYELLOW,LRED,LGREEN,LBLUE,plyellow,clear

dirs = listdir()
dirs = [d for d in dirs if isdir(d) and d[0].isalpha()]
ln = len(dirs)
cwd = getcwd()

for i,d in enumerate(dirs):
    try:
        plcyan(f'RUNNING {LYELLOW}{d.upper()} {LBLUE}({i+1}/{ln}){LRED}!')
        chdir(cwd)
        chdir(d)
        call("python file.py", shell=True)
    except KeyboardInterrupt:
        clear()
        continue

plyellow(f"TASKS {LGREEN}FINISHED{LRED}!")