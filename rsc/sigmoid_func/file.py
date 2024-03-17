from lib import *
from math import e
from matplotlib.pyplot import scatter, show
load_lib()

def g(y):
    return 1/(1+e**-y)

mx = "-10.0"
with open("data.csv", "w") as file:
    file.write("y,z\n")
    for i in range(-10,11,1):
        print(f"{LYELLOW}{equalize(str(float(i)),mx)[0]}: {LCYAN}{round(g(i))}")
        print(f"{LYELLOW}{equalize(str(float(i+0.5)),mx)[0]}: {LCYAN}{round(g(i+0.5))}")
        file.write(f"{i},{round(g(i))}\n")
        file.write(f"{i+0.5},{round(g(i+0.5))}\n")

data = fetch_data()
y,z = data['y'],data['z']
y,z = [float(yn) for yn in y],[float(zn) for zn in z]

scatter(y,z)

show()