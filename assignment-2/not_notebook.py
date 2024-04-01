"""This is where I will write all the code for Assignment 2 which will go in the notebook"""

import numpy as np
import matplotlib.pyplot as plt

# Generate array x that contains a sequence of numbers from -100 to 100 with steps of 0.5
x = np.arange(-100, 100.5, 0.5)
# Generate array y that is the cosine of x
y = np.cos(x)
# Generate array z that is the sine of x
z = np.sin(x)

# Plot both z and y vs x on the same axis
plt.plot(x, y)
plt.plot(x, z)
# Add a legend to the plot to name z and y
plt.legend(labels=("Y", "Z"))
# Add appropriate x- and y-axis labels
