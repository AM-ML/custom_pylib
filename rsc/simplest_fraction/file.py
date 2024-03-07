from subprocess import call
from lib import *

mout = "Enter Frac"
out = "Simplest"

out, mout = equalize(out, mout)

call("clear", shell=True)

frac = pgreeni(f"{mout}: ", t=0.02, color=CYAN)

frac = frac.split("/")
frac = [int(i.strip()) for i in frac]
a,b = frac
c = a if a < b else b

d = 1

for i in range(1,c+1):
    if a % i == 0 and b % i == 0:
       d = i

a1,b1 = (int) (a/d), (int) (b/d)

print()

pgreen(f"{out}: {CYAN}{a1} / {b1}", t=0.03)