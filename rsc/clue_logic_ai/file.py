from lib import plcyan,plred
import termcolor

from logic import *

mustard = Symbol("ColMustard")
plum = Symbol("ProfPlum")
scarlet = Symbol("MsScarlet")
characters = [mustard, plum, scarlet]

ballroom = Symbol("ballroom")
kitchen = Symbol("kitchen")
library = Symbol("library")
rooms = [ballroom, kitchen, library]

knife = Symbol("knife")
revolver = Symbol("revolver")
wrench = Symbol("wrench")
weapons = [knife, revolver, wrench]

symbols = characters + rooms + weapons


def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: YES", "green")
        elif not model_check(knowledge, Not(symbol)):
            termcolor.cprint(f"{symbol}: MAYBE", "light_yellow")


# There must be a person, room, and weapon.
knowledge = And(
    Or(mustard, plum, scarlet),
    Or(ballroom, kitchen, library),
    Or(knife, revolver, wrench)
)

check_knowledge(knowledge)
print()

cards = And(
    Not(mustard), Not(kitchen), Not(revolver)
)

# Initial cards
knowledge.add(cards)

plred(cards.formula())
print()

cards = Or(
    Not(scarlet), Not(library), Not(wrench)
)

# Unknown card
knowledge.add(cards)

plred(cards.formula())
print()

cards = And(Not(plum), Not(ballroom))

# Known cards
knowledge.add(cards)

plred(cards.formula())
print()

check_knowledge(knowledge)