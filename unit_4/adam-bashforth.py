exp = "(x*y)/2"
x = [0, 0.1, 0.2, 0.3]
y = [1, 1.01, 1.022, 1.023]
h = 0.1
n = 3  # dont change


def f(x, y):
    return eval(exp)


yp = y[n] + (h/24)*((55 * f(x[n], y[n])) - (59 * f(x[n-1], y[n-1])) + (37 * f(x[n-2], y[n-2])) - (9 * f(x[n-3], y[n-3])))
yc = y[n] + (h/24)*((9 * f(x[n] + h, yp)) + (19 * f(x[n], y[n])) - (5 * f(x[n-1], y[n-1])) + f(x[n-2], y[n-2]))
print("predtor : ", yp)
print("correction : ", yc)
