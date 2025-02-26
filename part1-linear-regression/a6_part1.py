import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("part1-linear-regression/blood_pressure_data.csv")
xAxis=data["Age"]
yAxis=data['Blood Pressure']
x = xAxis.values
y = yAxis.values
#print(data)

# Use reshape to turn the x values into 2D arrays:
x = x.reshape(-1,1)

# Create the model
model = LinearRegression().fit(x, y)
# Find the coefficient, bias, and r squared values.
# Each should be a float and rounded to two decimal places.
coef = round(float(model.coef_[0]),2)
intcpt = round(float(model.intercept_),2)
r_squared = model.score(x, y)
equation = coef*x + intcpt
# Print out the linear equation and r squared value
print(f"Equation: y = {coef}x + {intcpt} | r^2: {r_squared}")
# Predict the the blood pressure of someone who is 42 years old.
# Print out the prediction
x_predict=42
prediction = model.predict([[x_predict]])
print(prediction)

# Create the model in matplotlib and include the line of best fit
plt.xlabel("Age")
plt.ylabel("Systolic Blood Pressure")
plt.title("Systolic Blood Pressure by Age")
plt.scatter(x, y)
plt.plot(x, equation, c="r", label="Line of Best Fit")
plt.show()