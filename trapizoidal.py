# Trapezoidal Method for Numerical Integration

# Define the function to integrate
def f(x):
    return 1 / (1 + x**2)

# Implementing the Trapezoidal Method for Integration


def trapezoidal_integration(a, b, n):

    # Calculate the step size
    h = (b - a) / n

    # Initialize the integration result
    integration_result = f(a) + f(b)

    # Summing up intermediate values
    for i in range(1, n):
        x = a + i * h
        integration_result += 2 * f(x)

    # Final integration result
    integration_result *= h / 2

    # Display the result
    print(
        f"Integration result using Trapezoidal method: {integration_result:.6f}")


# Input Section
a = float(input("Enter the lower limit of integration: "))
b = float(input("Enter the upper limit of integration: "))
n = int(input("Enter the number of subintervals: "))


# Call the trapezoidal_integration() method
trapezoidal_integration(a, b, n)
