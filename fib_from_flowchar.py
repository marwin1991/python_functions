
def fib():
    num = int(input("Giva a fib number:"))
    x = 0
    y = 1
    while num >= x:
        z = x + y
        print(x)
        x = y
        y = z


fib()