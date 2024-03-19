from lib import gen_data, fetch_data
from sys import argv

gen_data(float(argv[1]),0)

print(fetch_data())
