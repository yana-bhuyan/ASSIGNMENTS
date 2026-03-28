import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df=pd_read_csv('diabetes[1].csv')

# Extract x and y values from the dataset
x=np.array(df['Glucose'])
y=np.array(df['DiabetesPedigreeFunction'])
Theta_1 = 0.0 # slope
Theta_0 = 0.0 # intercept
learning_rate = 0.0001
iterations = 1000

# Define the cost function (MSE) Mean Squared Error
def compute cost(x, y, Theta 1, Theta 0):
 m = len(y)
 prediction=Theta 1*x + Theta 0
 cost=(1/(2*m))*np.sum((prediction - y)**2)
 return cost

# Define the Grdient Descent
def gradient descent(x, y, Theta 1, Theta 0, learning rate):
 m = len(y)
 prediction = Theta 1*x + Theta 0
 d_1 = (1/m)*np.sum((prediction - y)*x)
 d_0 = (1/m)


