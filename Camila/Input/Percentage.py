def find_roots(a, b, c):
    # the equation is ax^2 + bx + c = 0
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        print("No real roots!")
    elif discriminant == 0:
        x = -b / (2 * a)
        print("x =", x)
    else:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        print("x1 =", x1)
        print("x2 =", x2)


a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

find_roots(a, b, c)