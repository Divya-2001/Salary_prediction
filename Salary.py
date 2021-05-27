import pandas as pd
import numpy
dataset = pd.read_csv('salarydata.csv')
X = dataset[['YearsExperience']]
y = dataset['Salary']
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X,y)
yrsExp = float(input("Enter years of Experience : "))
prediction = model.predict([[yrsExp]])
print("Your Salary would be : ", prediction)
