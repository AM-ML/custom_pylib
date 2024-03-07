from lib import gen_data,fetch,pcyani,YELLOW,pcyan,predi
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from matplotlib.pyplot import scatter, show
from subprocess import call

gen_data(1,0.7,0.5,0,max=10,rows=100)

x,y = fetch()

model = Pipeline(steps= [
    ("scale", StandardScaler()),
    ("model", LinearRegression())
])

model.fit(x,y)

preds = model.predict(x)

scatter(preds,y)

call("clear", shell=True)


ux = pcyani("enter x: ",color=YELLOW,t=0.03).strip().split(",")
ux = [float(xn) for xn in ux]
uy = model.predict([ux])

pcyan(f"Y Prediction: {YELLOW}{uy[0]:,.2f}",t=0.02)

print()

ushow = predi("Show results? ",color=YELLOW,t=0.03)

if ushow.lower() in ["y","yes","1","yeah","ya"]:
    show()
