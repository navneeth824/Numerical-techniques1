exp = "1 + y**2"
x0 = 0.9
y0 = 1.00185
h = 0.2

order = 4 # 2, 3, or 4
def f(x,y):
    return eval(exp)

k = []
k.append(h * f(x0,y0))
k.append(h* f(x0 + (h/2), y0 + (k[0]/2)))
dy = k[1]

if order == 3:
    k.append(h * f(x0 + h, y0 + (2*k[1]) - k[0]))
    dy = (1/6)* (k[0] + (3 * k[1]) + k[2])

if order == 4:
    k.append(h* f(x0 + (h/2), y0 + (k[1]/2)))
    k.append(h* f(x0 + h, y0 + k[2]))
    dy = (1/6)* (k[0] + (2 * k[1]) + (2 * k[2]) + k[3])

for ki in k:
    print(ki)

print("dy = ",dy)
print("y = ",y0+dy)
