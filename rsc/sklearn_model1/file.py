from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from matplotlib.pyplot import scatter,show
from sklearn.datasets import load_boston
from sklearn.pipeline import Pipeline
from pandas import DataFrame
from subprocess import call

pipe = Pipeline(steps = [
	("scale", StandardScaler()),
	("model", KNeighborsRegressor())
])

model = GridSearchCV(estimator=pipe, 
	param_grid={"model__n_neighbors":[1,2,3,4,5,6,7,8,9,10]},
	cv=3)
x,y = load_boston(return_X_y=True)

model.fit(x,y)
preds = model.predict(x)

call("clear",shell=True)

print(DataFrame(model.cv_results_))

scatter(preds,y)
show()
