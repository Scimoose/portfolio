import streamlit as st
import pandas as pd
import numpy as np
# Import keras libraries
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy


# Introduction
st.write("""
# Data Science Showcase App

""")

# Read and show dataset
dt = pd.read_csv("iris.csv")

st.write(dt)

x = dt.iloc[:, 1:4].values
y = pd.get_dummies(dt["Species"])
y = np.asarray(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3,
                                                    random_state=0)

# Build model
model = Sequential([
    Dense(units=10, input_dim=3, activation="relu"),
    Dense(units=10, activation="relu"),
    Dense(units=3, activation="softmax")
])

model.summary()

model.compile(optimizer=Adam(learning_rate=0.01),
              loss="categorical_crossentropy", metrics=["accuracy"])

st.write(dt.dtypes)


model.fit(X_train, y_train, batch_size=64, epochs=30, verbose=2)

y_pred = model.predict(X_test)
y_pred = np.argmax(y_pred, axis=1)

y_test = np.argmax(y_test, axis=1)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

st.write("""
This is the models confusion matrix:
""")
st.write(cm)
