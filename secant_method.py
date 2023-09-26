# Defining Function
def f(x):
    return 2.718281**(-x) - x

# Implementing Secant Method


def secant(a, b, e, N):
    print('\n\n*** SECANT METHOD IMPLEMENTATION ***')
    step = 1
    condition = True
    while condition:
        if f(a) == f(b):
            print('Divide by zero error!')
            break

        c = a - (b-a)*f(a)/(f(b) - f(a))
        # print('Iteration-%d, c = %0.6f and f(c) = %0.6f' % (step, c, f(c)))
        print(f"Iteration= {step}, c = {c:.6f} and f(c) = {f(c):.6f}")
        a = b
        b = c
        step = step + 1

        # if step > N:
        #     print('Not Convergent!')
        #     break

        condition = abs(f(c)) > e
    print('\n Required root is: %0.8f' % c)


# # Input Section
# a = float(input('Enter First Guess: '))
# b = float(input('Enter Second Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Maximum Step: '))

# Starting Secant Method
secant(0, 1, 0.000048, 3)
