import pandas as pd
from sklearn.linear_model import LinearRegression
from joblib import dump, load 
from sklearn.model_selection import train_test_split

png= pd.read_csv('pong_data.csv')


x = png[['ball_y']]
y = png['paddle_y']

model = LinearRegression(fit_intercept=True)
model.fit(x_train.values, y_train)
model.coef_
model.intercept_
ymodel=model.predict(x)


dump(model, 'mymodel.joblib')