from time import sleep
from subprocess import call
from random import randint, choice
from sys import exit
from cowsay import tux
from lib import RESET,LRED,LGREEN,LCYAN,LBLUE
import pyttsx3

global_counter = 0

def line(ctr):
	for i in range(1, 30):
		colors = [LRED,LGREEN,LCYAN,LBLUE]
		color = choice(colors)
		print(f"{color}$*/2{ctr*(randint(1, 103)/randint(1, 30))}{RESET}", end="")
	print()


def func():
	counter = 0
	breaker = int(200*(randint(1, 10)/randint(1,100)))

	while(True):
		breaker = int(200*(randint(1, 3)/randint(1,10)))
		sleep(0.01)
		if counter % breaker == 0:
			call("clear", shell=True)
			sleep(0.04)
		line(counter)
		counter+=1

def main():
	try:
		func()
	except KeyboardInterrupt:
		call("clear", shell=True)
		sleep(0.1)
		message = f"\033[1;6;91mDATA BREACH SUCCESSFUL!{LCYAN}"
		print(LCYAN,end="")
		tux(message)
		print(RESET,end="")
		engine = pyttsx3.init()

		engine.setProperty('rate', 180)
		engine.setProperty('volume',0.5)

		engine.say("DATA BREACH SUCCESSFUL!")

		engine.runAndWait()
		engine.stop()
		exit(0)

if __name__ == '__main__':
	main()

