from csv import DictReader
from collections import defaultdict
from lib import RESET
choices = defaultdict(lambda: {"played": 0, "won": 0, "lost": 0, "drawn": 0})

def process_row(row):
    user_choice = row["user_choice"]
    outcome = int(row["outcome"])

    choices[user_choice]["played"] += 1
    choices[user_choice]["won"] += outcome == 1
    choices[user_choice]["lost"] += outcome == -1
    choices[user_choice]["drawn"] += outcome == 0

def f():
    with open("rps.csv", "r") as f:
        file = DictReader(f)
        for row in file:
            process_row(row)

    print("data:")
    for choice, stats in choices.items():
        played = stats['played']
        percentage = played *100 / 100000
        won = stats['won']
        lost = stats['lost']
        drawn = stats['drawn']
        print(f"{choice}:")
        print(f"    played: {stats['played']:,} [ \033[1;96m{percentage:.2f}%{RESET} ] times")
        print(f"       won: {won:,} [ \033[1;96m{(won/played*100):.2f}%{RESET} ] times")
        print(f"      lost: {lost:,} [ \033[1;96m{(lost/played*100):.2f}%{RESET} ] times")
        print(f"     drawn: {drawn:,} [ \033[1;96m{(drawn/played*100):.2f}%{RESET} ] times\n")

def main():
    f()

if __name__ == '__main__':
    main()
