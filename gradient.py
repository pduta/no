import numpy as np
import matplotlib.pyplot as plt

def objective_function(x):
    return (x - 2)**2

def gradient(x):
    return 2 * (x - 2)

def gradient_descent(f, f_prime, x0, learning_rate=0.1, tol=1e-6, max_iter=1000):
    x = x0
    iterations = 0

    while iterations < max_iter:
        grad = f_prime(x)
        x -= learning_rate * grad

        if np.linalg.norm(grad) < tol:
            return x, f(x), iterations + 1  # Converged

        iterations += 1

    return x, f(x), iterations

# Example: Minimize the quadratic function f(x) = (x - 2)^2
initial_guess = 0.0
optimal_solution, optimal_value, num_iterations = gradient_descent(objective_function, gradient, initial_guess)

# Display the result
print("Optimal Solution (x):", optimal_solution)
print("Optimal Objective Value (f(x)):", optimal_value)
print("Number of Iterations:", num_iterations)

# Plot the function and the optimization path
x_values = np.linspace(-1, 4, 100)
y_values = objective_function(x_values)

plt.plot(x_values, y_values, label='Objective Function')
plt.scatter(optimal_solution, optimal_value, color='red', label='Optimal Solution')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gradient Descent Optimization')
plt.legend()
plt.show()
