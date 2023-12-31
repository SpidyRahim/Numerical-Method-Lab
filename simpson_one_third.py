# def f(x):
#     return 1/(1+x**2)


# a = float(input("Lower Limit = "))
# b = float(input("Upper Limit = "))
# n = int(input("Number of strips = "))
# h = (b-a)/n
# k = 1
# sum = 0

# while (k < n):
#     x = a + k*h
#     if (k % 2 == 0):
#         sum = sum + 2*f(x)
#     else:
#         sum = sum + 4*f(x)
#     k = k + 1

# Ia = (h/3)*(f(a)+f(b)+sum)
# print(f"Approximate Value Is {Ia}")


# Simpson's 1/3 Rule

# Define function to integrate
def f(x):
    return 1/(1 + x**2)

# Implementing Simpson's 1/3


def simpson13(a, b, n):
    
    # calculating step size
    h = (b - a) / n

    # Finding sum
    integration = f(a) + f(b)

    for i in range(1, n):
        k = a + i*h

        if i % 2 == 0:
            integration = integration + 2 * f(k)
        else:
            integration = integration + 4 * f(k)

    # Finding final integration value
    integration = integration * h/3

    # Display the result
    print(
        f"Integration result using Trapezoidal method: {integration:.6f}")


# Input Section
a = float(input("Enter the lower limit of integration: "))
b = float(input("Enter the upper limit of integration: "))
n = int(input("Enter the number of subintervals: "))

# Call simpson13() method and get result

simpson13(a, b, n)
