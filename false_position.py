# Defining Function
def f(x):
    return - 26 + (85*x) - (91*x**2) + (44*x**3) - (8*x**4) + (x**5)

# Implementing False Position Method


def falsePosition(a, b, e):
    iteration = 1
    print('\n\n*** FALSE POSITION METHOD IMPLEMENTATION ***')
    condition = True
    while condition:
        c = a - (b - a) * f(a) / (f(b) - f(a))
        f_c = f(c)
        print(f'Iteration-{iteration}, c = {c:.6f}, f(c) = {f_c:.6f}')

        if f(a) * f_c < 0:
            b = c
        else:
            a = c

        iteration += 1
        condition = abs(f_c) > e

    print(f'\nRequired root is: {c:.8f}')


# Input Section
a = float(input('First Guess (a): '))
b = float(input('Second Guess (b): '))
e = float(input('Tolerable Error: '))

# Checking Correctness of initial guess values and false positioning
if f(a) * f(b) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    falsePosition(a, b, e)
