from lib import *
from numpy import zeros

clear()

gen_data(1,0.7,0.5,0.3,0,max=6,rows=500)

x,y = fetch()
n = len(x[0])
w,b = zeros(n),0

alpha = 0.02
iters = 1000

gradient(w,b,x,y,alpha,iters,print=False)

rout = f"{YELLOW}1000: {BLUE}"

for wn in w:
    rout += f"{wn:,.2f} "

rout += f"{b:,.2f}"

pgreen(rout,t=0.03)

mout = "Enter X"
out  = "Y"

out,mout = equalize(out,mout)

ux = predi(f"{mout}: ",t=0.03,color=CYAN).split(",")
ux = [float(xn) for xn in ux]
uy = f(w,b,ux)
pred(f"{out}: {CYAN}{uy:,.2f}",t=0.03)