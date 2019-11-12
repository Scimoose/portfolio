# Support Vector Regression

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Position_Salaries.csv')

X = dataset.iloc[:, 1:2].values
Y = dataset.iloc[:, 2].values

#This is where I would split the data if I had more than 10

# Preprocessing
from sklearn.preprocessing import StandardScaler

sc_X = StandardScaler()
X = sc_X.fit_transform(X)

sc_Y = StandardScaler()
Y = sc_Y.fit_transform(Y.reshape(-1,1))

# Fitting SV Regression
from sklearn.svm import SVR
regressor = SVR() 
regressor.fit(X, Y)

# Predicting the test set values
Y_pred = regressor.predict(X)


# One value prediction
result = sc_Y.inverse_transform(regressor.predict(sc_X.transform([[6.5]])))

# Plot
plt.scatter(X, Y, color = 'green')
plt.plot(X, regressor.predict(X), color = 'yellow')
plt.title('Salary vs Experience')
plt.xlabel('Level of experience')
plt.ylabel('Salary')
plt.show()

plt.scatter(sc_X.inverse_transform(X), sc_Y.inverse_transform(Y), color = 'blue')
plt.plot(sc_X.inverse_transform(X), sc_Y.inverse_transform(regressor.predict(X)), color = 'yellow')
plt.title('Salary vs Experience')
plt.xlabel('Level of experience')
plt.ylabel('Salary')
plt.show()
