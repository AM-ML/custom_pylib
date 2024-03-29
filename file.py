from time import sleep
from time import time

t = time()

def smt(x,t=0.02,end="\n"):
	for i in x:
		print(i, end="",flush=True)
		sleep(t)
	print(end=end)

def smti(x,t=0.02,end=""):
	smt(x,t=t,end=end)
	return input("")

name = smti("hello? ").strip().title()

def cyanize(x):
	return f"\033[1;96m{x}\033[0;0m"

def yellowize(x):
	return f"\033[1;93m{x}\033[0;0m"

smt(cyanize(f"Greetings, {name}!"),t=0.03)

t= time() - t
t*= 1000

smt("finished in " + yellowize(f"{t:.0f}ms"), t=0)
