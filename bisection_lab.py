def bisection_method(func, a, b, error_accept):

    def f(x):
        f = eval(func)
        return f

    error = abs(b - a)

    while error > error_accept:
        c = (b + a) / 2

        if f(a) * f(b) >= 0:
            print(
                "No root or multiple roots are present in this and the bisection method won't perform")
            quit()

        elif f(a) * f(c) < 0:
            b = c
            error = abs(b - a)

        elif f(a) * f(c) < 0:
            a = c
            error = abs(b - a)

        else:
            print("Something went wrong")
            quit()

    print(f"The Error is {error}")
    print(f"The Root is {c}")
    # print(f"The lower boundary a is {a} and the upper boundary is {b}")

# to call our functions


bisection_method(
    "- 26 + (85*x) - (91*x**2) + (44*x**3) - (8*x**4) + (x**5)", 0.5, 1, 0.1)


# def bisection_method(func, a, b, tolerance, max_iterations=100):
#     if func(a) * func(b) >= 0:
#         print("Bisection method cannot guarantee convergence.")
#         return None

#     iteration = 0
#     while (b - a) / 2 > tolerance and iteration < max_iterations:
#         c = (a + b) / 2
#         if func(c) == 0:
#             return c  # Found the exact root
#         elif func(a) * func(c) < 0:
#             b = c
#         else:
#             a = c
#         iteration += 1

#     return (a + b) / 2  # Return the approximate root

# # Example usage:


# def example_function(x):
#     return -26 + (85*x) - (91*x**2) + (44*x**3) - (8*x**4) + (x**5)


# root = bisection_method(example_function, 0.5, 1, 0.1)
# if root is not None:
#     print(f"Approximate root: {root}")
