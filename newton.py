import numpy as np

def newton_method(f, f_prime, x0, tol=1e-6, max_iter=100):
    """
    Newton-Raphson method for optimization.

    Parameters:
    - f: Objective function
    - f_prime: Derivative of the objective function
    - x0: Initial guess
    - tol: Tolerance for convergence
    - max_iter: Maximum number of iterations

    Returns:
    - x_optimal: Optimal solution
    - f_optimal: Optimal objective value
    - iterations: Number of iterations performed
    """
    x = x0
    iterations = 0

    while iterations < max_iter:
        x_new = x - f(x) / f_prime(x)
        if np.abs(x_new - x) < tol:
            return x_new, f(x_new), iterations + 1  # Converged

        x = x_new
        iterations += 1

    return x, f(x), iterations

# Example: Minimize the quadratic function f(x) = x^2 - 4
f = lambda x: x**2 - 4
f_prime = lambda x: 2*x

initial_guess = 2.0
optimal_solution, optimal_value, num_iterations = newton_method(f, f_prime, initial_guess)

print("Optimal Solution (x):", optimal_solution)
print("Optimal Objective Value (f(x)):", optimal_value)
print("Number of Iterations:", num_iterations)
