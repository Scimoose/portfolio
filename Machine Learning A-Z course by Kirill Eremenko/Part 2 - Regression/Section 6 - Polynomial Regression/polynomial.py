# Polynomial regression (regresja wielomianowa)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Position_Salaries.csv')

# Split the dataset (we won't split it for training and test set, the data is too small)
X = dataset.iloc[:, 1:2].values
Y = dataset.iloc[:, 2].values

#Linear Regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X, Y)

#Predicting the test set values
Y_pred = regressor.predict(X)

    #Test set
plt.scatter(X, Y, color = 'green')
plt.plot(X, Y_pred, color = 'yellow')
plt.title('Salary vs Experience')
plt.xlabel('Level of experience')
plt.ylabel('Salary')
plt.show()

# Polynomial Regression
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4) # degree = 2 is default, changing might raise accuracy
X_poly = poly_reg.fit_transform(X)
lin_reg = LinearRegression()
lin_reg.fit(X_poly, Y)

Y_pred_two = lin_reg.predict(X_poly)

# Grid rearange for accuracy
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid)), 1)

plt.scatter(X, Y, color = 'green')
plt.plot(X_grid, lin_reg.predict(poly_reg.fit_transform(X_grid)), color = 'yellow')
plt.title('Salary vs Experience')
plt.xlabel('Level of experience')
plt.ylabel('Salary')
plt.show()

# Prediction of linear regression
regressor.predict(np.matrix([6.5]).reshape(-1,1))

# Prediction of polynomial
lin_reg.predict(poly_reg.fit_transform([[6.5]]))