# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# 1. NumPy Operations
# -------------------------------
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)
print("Sum of elements:", np.sum(arr))

# 2D Array operations
arr2 = np.array([[10,20,30],
                 [40,50,60],
                 [70,80,90]])

print("Row-wise sum:", np.sum(arr2, axis=1))
print("Column-wise sum:", np.sum(arr2, axis=0))

flattened = arr2.flatten()
print("Flattened array:", flattened)

unique_vals = np.unique(flattened)
print("Second maximum value:", unique_vals[-2])

# Matrix Multiplication
A = np.array([[1,2],
              [3,4]])
B = np.array([[5,6],
              [7,8]])

print("Matrix Multiplication Result:\n", A @ B)

# -------------------------------
# 2. Pandas Operations
# -------------------------------
data = {
    'X': [78,85,96,80,86],
    'Y': [84,94,89,83,86],
    'Z': [86,97,96,72,83]
}

df = pd.DataFrame(data)

# Element-wise operation
result = df['X'] ** (df['Y'] % 3)
print("Element-wise result:\n", result)

# DataFrame example
exam_data = {
    'name': ['Anastasia','Dima','Katherine','James','Emily'],
    'score': [12.5,9,16.5,np.nan,9],
    'attempts': [1,3,2,3,2],
    'qualify': ['yes','no','yes','no','no']
}

df2 = pd.DataFrame(exam_data)
print("First 3 rows:\n", df2.head(3))

# Handling missing values
filled = df2.fillna(df2.mean(numeric_only=True))
print("Filled missing values:\n", filled)

# -------------------------------
# 3. Data Visualization
# -------------------------------
x = [1,2,3,4,5]
y = [10,20,25,30,40]

# Line Plot
plt.plot(x, y)
plt.title("Line Plot")
plt.show()

# Bar Chart
plt.bar(x, y)
plt.title("Bar Chart")
plt.show()

# Scatter Plot
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()

# Histogram
data_hist = [1,2,2,3,3,3,4,4,5]
plt.hist(data_hist)
plt.title("Histogram")
plt.show()