def a(x, y, fucade):
    fucade += 1
    print("    " * fucade,"a() starts")
    print("    " * fucade,"a() gets parameters x:",x," y:",y)
    x = x + 1
    print("    " * fucade,"In a(), return:",x*y)
    return x * y

def b(z, fucade):
    fucade += 1
    print("    " * fucade,"b() starts")
    print("    " * fucade,"b() gets parameters z:",z)
    prod = a(z, z, fucade)
    print("    " * fucade,"print (z, prod)")
    print("    " * fucade,"b(), prod: ",prod)
    print("    " * fucade,"In b(), return prod")
    return prod

def c(x, y, z, fucade):
    fucade += 1
    print("    " * fucade,"c() starts")
    print("    " * fucade,"gets parameters x:",x," y:",y," z:",z)
    total = x + y + z
    square = b(total, fucade)**2
    print("    " * fucade,"c(), square:",square)
    print("    " * fucade,"In c(), return square")
    return square

x = 1
y = x + 1
fucade = 0
print("main starts")
print("In main(), x:",x)
print("In main(), y:",y)
print("c() return:",c(x, y+3, x+y, fucade))
