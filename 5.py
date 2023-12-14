# WAP to find Global Optimal Solution of a function 𝑓(𝑥) = −10𝐶𝑜𝑠(𝜋𝑥 − 2.2) + (𝑥 + 1.5)𝑥 graphically

import numpy as np
import matplotlib.pyplot as plt

# Define the objective function
def objective_function(x):
    return -10 * np.cos(np.pi * x - 2.2) + (x + 1.5) * x

# Generate x values
x_values = np.linspace(-5, 5, 1000)

# Calculate corresponding y values
y_values = objective_function(x_values)

# Plot the function
plt.plot(x_values, y_values, label='f(x)')

# Find the minimum point
min_x = x_values[np.argmin(y_values)]
min_y = min(y_values)

# Mark the minimum point on the graph
plt.scatter(min_x, min_y, color='red', label='Global Minimum')

# Add labels and legend
plt.title('Graph of f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

# Show the plot
plt.show()

# Display the optimal solution
print("Global Optimal Solution (x):", min_x)
print("Optimal Objective Value (f(x)):", min_y)
