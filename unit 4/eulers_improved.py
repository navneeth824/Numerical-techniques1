exp = "1 + y**2"
x0 = 0.4
h = 0.2
y0 = 0.41087
def f(x,y):
    return eval(exp)
print(y0 + (h/2) * (f(x0,y0) + f(x0+h,y0 + (h*f(x0,y0)))))
