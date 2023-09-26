# Defining Function
def f(x):
    return - 26 + (85*x) - (91*x**2) + (44*x**3) - (8*x**4) + (x**5)

# Implementing Bisection Method


def bisection(a, b, e):
    iteration = 1
    print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
    condition = True
    while condition:
        c = (a + b)/2
        print(f"Iteration-{iteration}, c = {c:.6f} and f(c) = {f(c):.6f}")

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        iteration = iteration + 1
        condition = abs(f(c)) > e

    print('\nRequired Root is : %0.8f' % c)


a = float(input('First Guess: '))
b = float(input('Second Guess: '))
e = float(input('Tolerable Error: '))


# Checking Correctness of initial guess values and bisecting
if f(a) * f(b) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    bisection(a, b, e)
