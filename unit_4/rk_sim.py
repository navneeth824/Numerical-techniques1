exp1 = "x + z" # f(x)
exp2 = "x - y" # g(x)
x0 = 0
y0 = 0
z0 = 1
h = 0.1

def f(x,y,z):
    return eval(exp1)

def g(x,y,z):
    return eval(exp2)

k = []
l = []
k.append(h * f(x0,y0,z0))
l.append(h * g(x0,y0,z0))
k.append(h* f(x0 + (h/2), y0 + (k[0]/2), z0 + (l[0]/2)))
l.append(h* g(x0 + (h/2), y0 + (k[0]/2), z0 + (l[0]/2)))
k.append(h* f(x0 + (h/2), y0 + (k[1]/2), z0 + (l[1]/2)))
l.append(h* g(x0 + (h/2), y0 + (k[1]/2), z0 + (l[1]/2)))
k.append(h* f(x0 + h, y0 + k[2], z0 + l[2]))
l.append(h* g(x0 + h, y0 + k[2], z0 + l[2]))
dy = (1/6)* (k[0] + (2 * k[1]) + (2 * k[2]) + k[3])
dz = (1/6)* (l[0] + (2 * l[1]) + (2 * l[2]) + l[3])

for i in range(4):
    print("k",i+1,"=",k[i])
    print("l",i+1,"=",l[i])

print("dy = ",dy)
print("y = ",y0+dy)

print("dz = ",dz)
print("z = ",z0+dz)
