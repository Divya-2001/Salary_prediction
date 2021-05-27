import pandas as pd
dataset = pd.read_csv('salarydata.csv')
X = dataset[['YearsExperience']]
y = dataset['Salary']
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X,y)
import joblib
joblib.dump(model, 'finalsalary.pk1')
