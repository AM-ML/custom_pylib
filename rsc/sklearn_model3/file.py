from pandas import read_csv
from lib import pyellow

pyellow("lib loaded!")

df = read_csv("data.csv")

df.head(3)

