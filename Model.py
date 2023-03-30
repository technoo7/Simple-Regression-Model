import numpy as np #Importing
import matplotlib.pyplot as plt #Importing

# Creating Input Data as a Python List
x = [1,2,5,7,6]
y = [2,5,9,4,7]

# Converting x, y List to NumPy Arrays using the np.array() Function
x = np.array(x)
y = np.array(y)

# Simple Linear Regression Model - m*x + b
# m = slope, b = intercept of Regression Line, x = variable

# Using the np.polyfit Function to compute the slope and y-intercept of the regression
m, b = np.polyfit(x,y,2)
prediction = m*x + b

# Plot The Data and The R.L
plt.scatter(x,y)
plt.plot(x,prediction,color = "red")
plt.show()