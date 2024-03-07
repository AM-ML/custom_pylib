from lib import pcyan,predi,CYAN
from time import sleep

pcyan("Hello, world!", t=0.03)

sleep(0.7)

name = predi("What's your name? ",t=0.02,color=CYAN).strip().title()

sleep(0.4)

pcyan(f"\nHello, {name}!",t=0.015)
