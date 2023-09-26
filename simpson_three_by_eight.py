# Simpson's 3/8 Rule

# Define function to integrate
def f(x):
    return 1/(1 + x**2)

# Implementing Simpson's 3/8


def simpson13(a, b, n):

    # calculating step size
    h = (b - a) / n

    # Finding sum
    integration = f(a) + f(b)

    for i in range(1, n):
        k = a + i*h

        if i % 3 == 0:
            integration = integration + 2 * f(k)
        else:
            integration = integration + 3 * f(k)

    # Finding final integration value
    integration = integration * 3 * h / 8

    # Display the result
    print(
        f"Integration result using Trapezoidal method: {integration:.6f}")


# Input Section
a = float(input("Enter the lower limit of integration: "))
b = float(input("Enter the upper limit of integration: "))
n = int(input("Enter the number of subintervals: "))

# Call simpson13() method and get result

simpson13(a, b, n)
