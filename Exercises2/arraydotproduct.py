import numpy as np

# Define the vector
v = np.array([2., 2., 4.])

# Define the coordinate axes
e0 = np.array([1, 0, 0])
e1 = np.array([0, 1, 0])
e2 = np.array([0, 0, 1])

# Project the vector onto each axis
projection_e0 = np.dot(v, e0)
projection_e1 = np.dot(v, e1)
projection_e2 = np.dot(v, e2)

# Print the results
print(f"Projection onto e0: {projection_e0}")
print(f"Projection onto e1: {projection_e1}")
print(f"Projection onto e2: {projection_e2}")
