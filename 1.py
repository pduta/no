
#WAP for finding optimal solution using Line Search method.

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

# Define the objective function
def objective_function(x):
    return x**2 - 4*x + 4

# Define the derivative of the objective function (gradient)
def gradient(x):
    return 2*x - 4

# Armijo line search method
def armijo_line_search(f, grad, x, alpha=1.0, beta=0.5, max_iter=100):
    for _ in range(max_iter):
        if f(x + alpha * grad(x)) <= f(x) + beta * alpha * np.dot(grad(x), grad(x)):
            return alpha
        alpha *= beta
    return alpha

# Gradient Descent with Armijo Line Search
def gradient_descent_armijo(x0, f, grad, max_iter=1000, tol=1e-6):
    x = x0
    for _ in range(max_iter):
        gradient_value = grad(x)
        step_size = armijo_line_search(f, grad, x)
        x = x - step_size * gradient_value
        if np.abs(gradient_value) < tol:
            break
    return x

# Plot the objective function
x_values = np.linspace(-1, 6, 100)
y_values = objective_function(x_values)

plt.plot(x_values, y_values, label='Objective Function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Objective Function')

# Find the optimal solution using gradient descent with Armijo line search
initial_guess = 5.0
optimal_solution = gradient_descent_armijo(initial_guess, objective_function, gradient)

# Mark the optimal solution on the graph
plt.scatter(optimal_solution, objective_function(optimal_solution), color='red', label='Optimal Solution')
plt.legend()

# Show the plot
plt.show()

# Display the result
print("Optimal Solution (x):", optimal_solution)
print("Optimal Objective Value (f(x)):", objective_function(optimal_solution))
