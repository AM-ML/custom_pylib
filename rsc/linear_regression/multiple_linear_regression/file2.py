from lib import *
from numpy import zeros
from time import time

x,y = fetch()

m,n = len(y), len(x[0])

w,b = zeros(n), 0

alpha = 0.035
iters = 500

t= time()

gradient(w,b,x,y,alpha,iters,print=False)

t = time() - t
t *= 1000

wb = [float(f"{wn:.2f}") for wn in w]
print("\033[1;96m--->>",*wb,b,sep="   ")
plred(f"FINISHED IN {LYELLOW}{t:.0f}ms{LRED}!")

xb = [float(xn) for xn in plbluei("enter x: ",color=LYELLOW).split(",")]
y = f(w,b,xb)

plblue(f"Y prediction: {LGREEN}{y:.2f}")