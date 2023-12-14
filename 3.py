#WAP to compute the gradient and Hessian of the function

import numpy as np
from scipy.optimize import least_squares

def rosen(x):
    return np.sum(100 * (x[1:] - x[:-1]**2)**2 + (1 - x[:-1]**2)**2)

# Initial guess
initial_guess = np.array([1, 3])

# Using least_squares
res = least_squares(rosen, initial_guess)

# Print the result
print("Optimized x:", res.x)
