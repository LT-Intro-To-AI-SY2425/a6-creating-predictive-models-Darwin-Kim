import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

'''
**********CREATE THE MODEL**********
'''

data = pd.read_csv("part2-training-testing-data/blood_pressure_data.csv")
x = data["Age"].values
y = data["Blood Pressure"].values
print(x)
x = x.reshape(-1,1)
print(x)
# Create your training and testing datasets:
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=.2)
# Use reshape to turn the x values into 2D arrays:

# Create the model
model = LinearRegression().fit(xtrain, ytrain)
# Find the coefficient, bias, and r squared values. 
# Each should be a float and rounded to two decimal places. 
coef = round(float(model.coef_[0]), 2)
intcpt = round(float(model.intercept_), 2)
rSquared = model.score(xtrain,ytrain)
equation=coef*x + intcpt
# Print out the linear equation and r squared value:
print(f"Equation: y = {coef}x + {intcpt}, r^2:{rSquared}")

'''
**********TEST THE MODEL**********
'''
# reshape the xtest data into a 2D array
#print(x)
#print(xtrain)
# get the predicted y values for the xtest values - returns an array of the results
predict = model.predict(xtest)
# round the value in the np array to 2 decimal places
predict = np.around(predict, 2)

# Test the model by looping through all of the values in the xtest dataset
print("\nTesting Linear Model with Testing Data:")
for i in range(len(xtest)):
    actual=ytest[i]
    predicted=predict[i]
    x=xtest[i]
    dist=actual-predicted
    print(f"x value:{float(x[0])} Predicted y value: {predicted} Actual y value: {actual} distance: {abs(round(dist,2))}")

'''
**********CREATE A VISUAL OF THE RESULTS**********
'''
#sets the size of the graph
plt.figure(figsize=(5,4))

#creates a scatter plot and labels the axes
plt.scatter(xtrain,ytrain, c="purple", label="Training Data")
plt.scatter(xtest, ytest, c="blue", label="Testing Data")

plt.scatter(xtest, predict, c="red", label="Predictions")

plt.xlabel("Age")
plt.ylabel("Blood pressure")
plt.title("Blood pressure VS Age")
#print(x)
#print(xtrain)
plt.plot(xtrain, coef*xtrain + intcpt, c="b", label="Line of Best Fit")
plt.legend()
plt.show()