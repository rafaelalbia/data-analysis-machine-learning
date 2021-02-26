def sumSquare(a, b):
    sumSqr = a**2 + b**2
    return sumSqr

print(sumSquare(2, 3))

sumSquare2 = lambda a, b : a**2 + b**2
print(sumSquare2(2, 3))

x = lambda f : f / 2
print(x(10))
