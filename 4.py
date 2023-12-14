#WAP to find Global Optimal Solution of a function
#𝑓(𝑥) = −10𝐶𝑜𝑠(𝜋𝑥 − 2.2) + (𝑥 + 1.5)𝑥 algebraically

import numpy as np
from scipy.optimize import minimize

# Define the objective function
def objective_function(x):
    return -10 * np.cos(np.pi * x - 2.2) + (x + 1.5) * x

# Provide an initial guess
initial_guess = 0.0

# Find the global optimal solution
result = minimize(objective_function, initial_guess, method='BFGS')

# Display the result
if result.success:
    print("Global Optimal Solution:", result.x)
    print("Optimal Objective Value:", result.fun)
else:
    print("Optimization failed:", result.message)
