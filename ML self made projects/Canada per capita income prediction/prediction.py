import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("canada_per_capita_income.csv")

X = dataset[['year']]
Y = dataset[["per capita income (US$)"]]

plt.scatter(X,Y, c="blue", marker="+")
plt.ylabel("Income per capita")
plt.xlabel("Year")
plt.title("Canada per capita yearly income")
plt.show()

# Importing a linear regression model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X, Y)

Y_pred_linear = regressor.predict([[2000],[2020]])

plt.scatter(dataset['year'], dataset['per capita income (US$)'], marker="+")
plt.xlabel("Year")
plt.ylabel("Income per capita")
plt.title("Canada per capita yearly income")
plt.plot(dataset['year'], regressor.predict(dataset[["year"]]),color="blue")
