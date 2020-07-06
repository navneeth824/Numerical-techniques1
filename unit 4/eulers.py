exp = "1 + y**2"
x0 = 0.2
h = 0.2
y0 = 0.202666
def f(x,y):
    return eval(exp)

print(y0 + h * f(x0,y0))
