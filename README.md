# ML-projects
My struggles and experiments with ML

import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

import os

os.getcwd()

os.chdir('C:\\Users\\Subhadeep Sarkar\\Downloads')

table=pd.read_csv("MArket data.csv")

table




%matplotlib inline
plt.xlabel('area(sqr mtrs)')
plt.ylabel('price(Rs)')
plt.scatter(table.area,table.price,color='cyan',marker='o')


new_table = table.drop('price',axis='columns')
new_table

price=table.price

reg = linear_model.LinearRegression()
reg.fit(new_table,table.price)

 reg.predict([[3300]])

reg.coef_

reg.intercept_

areatable=pd.read_csv("area.csv")

areatable

reg_areatable=reg.predict(areatable)
reg_areatable

areatable['prices']= reg_areatable

areatable

areatable.to_csv("Predictions.csv")

Predictions=pd.read_csv("Predictions.csv")
Predictions

