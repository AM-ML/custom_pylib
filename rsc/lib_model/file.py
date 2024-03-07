from lib import gen_data, fetch, gradient,f,RESET,pcyani,pcyan
from numpy import zeros

gen_data(1,0.7,0.5,0,max=6,rows=20)

x,y = fetch()

n = len(x[0])
m = len(y)

w,b = zeros(n),0

iters = 1000
alpha = 0.03

gradient(w,b,x,y,alpha,iters)

ux = pcyani(f"Enter x: ",t=0.04).strip().split(",")
ux = [float(uxn) for uxn in ux]
ypred = f(w,b,ux)
pcyan(f"Y prediction: {RESET}{ypred:,.2f}",t=0.02)
