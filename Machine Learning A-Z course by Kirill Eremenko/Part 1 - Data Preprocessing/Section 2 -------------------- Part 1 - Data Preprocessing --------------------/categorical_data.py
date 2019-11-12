# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Importing the dataset
dataset = pd.read_csv('Data.csv')

X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values

#Encoding data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import make_column_transformer

preprocessor = make_column_transformer( (OneHotEncoder(),[0]),remainder="passthrough")
X = preprocessor.fit_transform(X)

labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)