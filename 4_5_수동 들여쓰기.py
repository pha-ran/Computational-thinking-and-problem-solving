def a(x, y):
    print("            a() starts")
    print("            a() gets parameters x:",x ," y:", y)
    x = x + 1
    print("            In a(), return:", x*y)
    return x * y

def b(z):
    print("        b() starts")
    print("        b() gets parameters z:", z)
    prod = a(z, z)
    print("        print (z, prod)")
    print("        b(), prod: ", prod)
    print("        In b(), return prod")
    return prod

def c(x, y, z):
    print("    c() starts")
    print("    gets parameters x:",x ," y:", y, " z:", z)
    total = x + y + z
    square = b(total)**2
    print("    c(), square:", square)
    print("    In c(), return square")
    return square

x = 1
y = x + 1
print("main starts")
print("In main(), x:", x)
print("In main(), y:", y)
print("c() return:", c(x, y+3, x+y))
