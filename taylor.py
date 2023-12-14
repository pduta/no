import sympy as sp

def taylor_polynomial(func, x0, degree):
    """
    Compute the Taylor polynomial for a given function.

    Parameters:
    - func: The function for which the Taylor polynomial is to be calculated
    - x0: The point around which the Taylor series is expanded
    - degree: The degree of the Taylor polynomial

    Returns:
    - taylor_poly: The Taylor polynomial
    """
    x = sp.symbols('x')
    taylor_series = sp.series(func, x, x0, degree + 1).removeO()
    taylor_poly = sp.Poly(taylor_series, x)
    return taylor_poly

# Example: Taylor polynomial for sin(x) around x=0 of degree 3
x = sp.symbols('x')
func = sp.sin(x)
degree = 3
x0 = 0

taylor_poly = taylor_polynomial(func, x0, degree)

# Display the Taylor polynomial
print("Taylor Polynomial:", taylor_poly)
