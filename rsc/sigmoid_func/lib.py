from csv import DictReader
from time import sleep
from numpy import array,sum,dot
from random import randint
from subprocess import call
from math import exp

def sigmoid(y) -> float:
    return 1 / (1 + exp(-y))

RED = '\033[91m'
LRED = '\033[1;31m'
GREEN = '\033[92m'
LGREEN = '\033[1;32m'
YELLOW = '\033[93m'
LYELLOW = '\033[1;33m'
BLUE = '\033[94m'
LBLUE = '\033[1;34m'
CYAN = '\033[96m'
LCYAN = '\033[1;36m'
RESET = '\033[0m'
LRESET = '\033[1;0m'

def confirm(prompt,pcolor=LBLUE,ucolor=CYAN,t=0):
	conf = pcolori(prompt,pcolor=pcolor,ucolor=ucolor,t=t)
	if conf.lower() in ['y','yes','yeah','ya','1']:
		return True
	else:
		return False

def reset_color():
    print(RESET,end="")

def pred(output, t=0,end="\n"):
    smt(f"{RED}{output}{RESET}", t=t,end=end)

def pgreen(output, t=0, end="\n"):
    smt(f"{GREEN}{output}{RESET}",t=t, end=end)

def pyellow(output, t=0, end="\n"):
    smt(f"{YELLOW}{output}{RESET}", t=t,end=end)

def pblue(output, t=0, end="\n"):
    smt(f"{BLUE}{output}{RESET}", t=t,end=end)

def pcyan(output, t=0, end="\n"):
    smt(f"{CYAN}{output}{RESET}", t=t,end=end)

def pcolor(output,color=RESET,t=0,end="\n"):
    smt(f"{color}{output}{RESET}",t=t,end=end)

def pgreeni(prompt,color=RESET,t=0):
    pgreen(prompt,end="",t=t)
    uin = input(f"{color}")
    reset_color()
    return uin

def load_lib():
    clear()
    pcolor("loaded library!",color=LGREEN)
    print()

def pcyani(prompt,color=RESET,t=0):
    pcyan(prompt,end="",t=t)
    uin = input(f"{color}")
    reset_color()
    return uin

def pcolori(prompt,pcolor=RESET, ucolor=RESET,t=0):
    smt(f"{pcolor}{prompt}{RESET}",end="",t=t)
    uin = input(f"{ucolor}")
    reset_color()
    return uin

def predi(prompt,color=RESET,t=0):
    pred(prompt,end="",t=t)
    uin = input(f"{color}")
    reset_color()
    return uin

def pbluei(prompt,color=RESET,t=0):
    pblue(prompt,end="",t=t)
    uin = input(f"{color}")
    reset_color()
    return uin

def pyellowi(prompt,color=RESET,t=0):
    pyellow(prompt,end="",t=t)
    uin = input(f"{color}")
    reset_color()
    return uin

def fetch():
    x,y = [], []
    with open("data.csv", "r") as file:
        fl = DictReader(file)
        for row in fl:
            x.append([float(row[key]) for key in list(row.keys()) if "x" in key])
            y.append(float(row["y"]))

    return array(x), array(y)

def f(w,b,x):
    return dot(w,x)+b

def gradient(w,b,x,y,alpha,iters,print=True):
    m = len(y)
    n = len(w)

    mout = f"{iters}"

    for iter in range(iters+1):

        preds = [f(w,b,xn) for xn in x]
        errs = preds-y

        for i in range(n):
            w[i] = w[i] - alpha / m * sum(errs * x[:, i])
        b = b - alpha * sum(errs)/m

        if iter % 10 == 0 and print==True:
            out = f"{iter}"

            while len(out) < len(mout):
                out = " " + out

            pyellow(f"{out}: {RESET}", end="")
            for nn in range(n):
                pblue(f"{w[nn]:.2f} ", end="")
            pblue(f"{b:.2f}")

def gen_data(*args,max=6,rows=20):
    w,b = [],0
    
    for i in range(len(args)-1):
        w.append(args[i])
    b = args[-1]

    with open("data.csv", "w") as file:
        for i in range(len(w)):
            file.write(f"x{i+1},")
        file.write(f"y\n")

        for i in range(1,rows+1):
            x = [randint(1,max+1) for _ in range(len(w))]
            xnew = [x[e] * w[e] for e in range(len(w))]
            y = sum(xnew) + b

            for xn in x:
                file.write(f"{xn},")
            file.write(f"{y}\n")

def smt(x,t=0.02, end="\n"):
	for i in x:
		print(i, flush=True, end="")
		sleep(t)
	print(end=end)

def smti(x,t=0.02):
	smt(x,t,end="")
	return input("")

def equalize(a,b):

    if len(a) < len(b):
        while len(a) < len(b):
            a = " " + a
    else:
        while len(b) < len(a):
            b = " " + b

    return a,b

def clear():
    call("clear", shell=True)


def fetch_data(*args,list=False):
    sects = {}
    lst = []
        
    with open("data.csv", "r") as file:
        fl = DictReader(file)

        keys = args if args else fl.fieldnames 
        for key in keys:
            sects[key] = []

        if list:
            for row in fl:
                lst.append(row)
            return lst
        for row in fl:
            for key in keys:
                sects[key].append(row[key])
    return sects

def insert_data(arr:array):
    with open("data.csv", "a") as file:
        for i in arr[:-1]:
            file.write(f"{i},")
        file.write(f"{arr[-1]}\n")


def plred(output, t=0,end="\n"):
    smt(f"{LRED}{output}{RESET}", t=t,end=end)

def plgreen(output, t=0, end="\n"):
    smt(f"{LGREEN}{output}{RESET}",t=t, end=end)

def plyellow(output, t=0, end="\n"):
    smt(f"{LYELLOW}{output}{RESET}", t=t,end=end)

def plblue(output, t=0, end="\n"):
    smt(f"{LBLUE}{output}{RESET}", t=t,end=end)

def plcyan(output, t=0, end="\n"):
    smt(f"{LCYAN}{output}{RESET}", t=t,end=end)

def plgreeni(prompt,color=RESET,t=0):
    plgreen(prompt,end="",t=t)
    uin = input(f"{color}")
    reset_color()
    return uin

def plcyani(prompt,color=RESET,t=0):
    plcyan(prompt,end="",t=t)
    uin = input(f"{color}")
    reset_color()
    return uin

def plredi(prompt,color=RESET,t=0):
    plred(prompt,end="",t=t)
    uin = input(f"{color}")
    reset_color()
    return uin

def plbluei(prompt,color=RESET,t=0):
    plblue(prompt,end="",t=t)
    uin = input(f"{color}")
    reset_color()
    return uin

def plyellowi(prompt,color=RESET,t=0):
    plyellow(prompt,end="",t=t)
    uin = input(f"{color}")
    reset_color()
    return uin