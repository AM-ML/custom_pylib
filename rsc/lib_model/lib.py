from csv import DictReader
from time import sleep
from numpy import array,sum,dot
from random import randint

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
RESET = '\033[0m'

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

def gradient(w,b,x,y,alpha,iters):
    m = len(y)
    n = len(w)

    mout = f"{iters}"

    for iter in range(iters+1):

        preds = [f(w,b,xn) for xn in x]
        errs = preds-y

        for i in range(n):
            w[i] = w[i] - alpha / m * sum(errs * x[:, i])
        b = b - alpha * sum(errs)/m

        if iter % 10 == 0:
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

