import matplotlib.pyplot as plt
import numpy as np

# Generate data for the downward facing V shape
x = np.linspace(1, 3, 400)
y = np.interp(x, [1, 2, 3], [2, 4, 1])  # Create a downward V shape starting at (1, 2), peak at (2, 4), and ending at (3, 1)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.title('Sample Graph!')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Set axis limits
plt.xlim(1, 3)
plt.ylim(1, 4)

# Show the plot
plt.show()
