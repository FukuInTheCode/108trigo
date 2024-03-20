import numpy as np
import matplotlib.pyplot as plt

# Create a sample matrix
matrix = np.random.rand(5, 5)

# Plot the matrix
plt.imshow(matrix, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.title('Matrix Visualization')
plt.show()
