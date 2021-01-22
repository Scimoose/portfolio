# Analyzing esport trends with machine learning

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set()


df = pd.read_csv('esports_revenue.csv')
year = df[['Year']]
revenue = df[['Estimated e-sports market revenue in million dollars']]
audience = df[['Audience']]
freq_viewers = df[['Frequent viewers in million']]
oc_viewers = df[['Occasional viewers in million']]

# Revenue plot
plt.scatter(year,revenue, c="blue", marker="+")
plt.ylabel("E-sports revenue")
plt.xlabel("Year")
plt.title("Revenue each year")
plt.show()

# Audience plot
plt.scatter(year,audience, c="blue", marker="+")
plt.ylabel("E-sports audience")
plt.xlabel("Year")
plt.title("Audience each year")
plt.show()

# Frequent audience plot
plt.scatter(year,freq_viewers, c="blue", marker="+")
plt.ylabel("E-sports frequent audience")
plt.xlabel("Year")
plt.title("Frequent audience each year")
plt.show()

# Occasional audience plot
plt.scatter(year,oc_viewers, c="blue", marker="+")
plt.ylabel("E-sports occasional audience")
plt.xlabel("Year")
plt.title("Occasional audience each year")
plt.show()

### Analyzing revenue

# Importing a linear regression model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(year, revenue)

regressor.predict([[2022]])

plt.scatter(year,revenue, c="blue", marker="+")
plt.plot(year, regressor.predict(year), c='blue')
plt.ylabel("E-sports revenue")
plt.xlabel("Year")
plt.title("")
plt.show()


# Polynomial Regression
X = df.iloc[:,0].values
Y = df.iloc[:,1].values
X = X.reshape(-1, 1)

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 3) # degree = 2 is default, changing might raise accuracy
X_poly = poly_reg.fit_transform(X)
lin_reg = LinearRegression()
lin_reg.fit(X_poly, Y)

Y_pred = lin_reg.predict(X_poly)

# Grid rearange for accuracy
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid)), 1)

plt.scatter(X, Y, color = 'green')
plt.plot(X_grid, lin_reg.predict(poly_reg.fit_transform(X_grid)), color = 'yellow')
plt.ylabel("E-sports revenue")
plt.xlabel("Year")
plt.title("")
plt.show()

# Prediction of polynomial
lin_reg.predict(poly_reg.fit_transform([[2022]]))


year = year[1:]
revenue = revenue[1:]
# Importing the second linear regression model
from sklearn.linear_model import LinearRegression
regressor_two = LinearRegression()
regressor_two.fit(year, revenue)

regressor_two.predict([[2020],[2021],[2022]])

plt.scatter(year,revenue, c="blue", marker="+")
plt.plot(year, regressor_two.predict(year), c='blue')
plt.ylabel("E-sports revenue")
plt.xlabel("Year")
plt.title("")
plt.show()

### Analysing audience trends

# Polynomial Regression
X = df.iloc[:,0].values
Y = df.iloc[:,-1].values
X = X.reshape(-1, 1)

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 3) # degree = 2 is default, changing might raise accuracy
X_poly = poly_reg.fit_transform(X)
lin_reg = LinearRegression()
lin_reg.fit(X_poly, Y)

Y_pred = lin_reg.predict(X_poly)

# Grid rearange for accuracy
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid)), 1)

plt.scatter(X, Y, color = 'green')
plt.plot(X_grid, lin_reg.predict(poly_reg.fit_transform(X_grid)), color = 'yellow')
plt.ylabel("E-sports revenue")
plt.xlabel("Year")
plt.title("")
plt.show()


# Importing a linear regression model
from sklearn.linear_model import LinearRegression
year = df[['Year']]
regressor = LinearRegression()
regressor.fit(year, audience)

regressor.predict([[2022]])

plt.scatter(year,audience, c="blue", marker="+")
plt.plot(year, regressor.predict(year), c='blue')
plt.ylabel("E-sports revenue")
plt.xlabel("Year")
plt.title("")
plt.show()

# Importing second LRM, for frequent audience
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(year, freq_viewers)

regressor.predict([[2022]])

plt.scatter(year,freq_viewers, c="blue", marker="+")
plt.plot(year, regressor.predict(year), c='blue')
plt.ylabel("E-sports revenue")
plt.xlabel("Year")
plt.title("")
plt.show()

# Importing third LRM, for occasional audience
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(year, oc_viewers)

regressor.predict([[2022]])

plt.scatter(year, oc_viewers, c="blue", marker="+")
plt.plot(year, regressor.predict(year), c='blue')
plt.ylabel("E-sports revenue")
plt.xlabel("Year")
plt.title("")
plt.show()