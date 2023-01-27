import math
def triangle_area(x, y):
    return x * y / 2
def rectangle_area(x, y):
    return x * y
def quadrangle_area(x, y, z, t):
    hypotenuse = math.sqrt(x + y)
    return rectangle_area(x, y) + triangle_area(z, t) + triangle_area(z, hypotenuse) + triangle_area(t, hypotenuse)
x = 3
y = 4
z = 5
t = 6

result = quadrangle_area(x, y, z, t)
print(result)

# task2 
print('{:0>10}'.format(oct(int(result))))

