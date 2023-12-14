#WAP to solve constraint optimization problem

from scipy.optimize import minimize

# Define the objective function
def objective_function(x):
    return (x[0] - 2)**2 + (x[1] - 3)**2

# Define the inequality constraints
def constraint1(x):
    return 4 - x[0] - x[1]

def constraint2(x):
    return x[0] - x[1] - 1

# Define the bounds for x1 and x2
bounds = [(0, None), (0, None)]

# Define the constraints
constraints = [
    {'type': 'ineq', 'fun': constraint1},
    {'type': 'ineq', 'fun': constraint2}
]

# Initial guess
initial_guess = [0, 0]

# Solve the constrained optimization problem
result = minimize(objective_function, initial_guess, bounds=bounds, constraints=constraints)

# Display the result
print("Optimal Solution (x):", result.x)
print("Optimal Objective Value (f(x)):", result.fun)
