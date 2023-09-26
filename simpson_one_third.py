def f(x):
    return 1/(1+x**2)


a = float(input("Lower Limit = "))
b = float(input("Upper Limit = "))
n = int(input("Number of strips = "))
h = (b-a)/n
k = 1
sum = 0

while (k < n):
    x = a + k*h
    if (k % 2 == 0):
        sum = sum + 2*f(x)
    else:
        sum = sum + 4*f(x)
    k = k + 1

Ia = (h/3)*(f(a)+f(b)+sum)
print(f"Approximate Value Is {Ia}")
