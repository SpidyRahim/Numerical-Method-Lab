import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**3 + 2*x**2 - x + 8


def bisection_method(a, b, tol):
    if f(a) * f(b) >= 0:
        print("Bisection method may not converge on the given interval.")
        return None

    approx_roots = []
    iterations = 0

    while (b - a) / 2.0 > tol:
        midpoint = (a + b) / 2.0
        approx_roots.append(midpoint)
        if f(midpoint) == 0.0:
            return midpoint, approx_roots
        elif f(a) * f(midpoint) < 0.0:
            b = midpoint
        else:
            a = midpoint
        iterations += 1

    root = (a + b) / 2.0
    approx_roots.append(root)
    return root, approx_roots, iterations


# Define the interval [a, b] and tolerance
a = -10.0
b = 10.0
tolerance = 1e-6

root, approx_roots, iterations = bisection_method(a, b, tolerance)

if root is not None:
    print(f"Approximate root found: {root:.6f}")
    print(f"f({root:.6f}) = {f(root):.6f}")
    print(f"Iterations needed: {iterations}")
else:
    print("Bisection method did not converge.")

# Create a graphical representation
x = np.linspace(-10, 10, 400)
y = f(x)

plt.plot(x, y, label='f(x)')
plt.axhline(0, color='red', linestyle='--', label='y=0')
plt.plot(approx_roots, [0] * len(approx_roots),
         'ro', label='Approximate Roots')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Bisection Method Visualization')
plt.legend()
plt.grid()
plt.show()
