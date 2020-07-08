exp = "(x+y)/2"
x = [0,0.5,1,1.5]
y = [2,2.636,3.597,4.968]
h = 0.5
n = 3 # dont change

def f(x,y):
    return eval(exp)

yp = y[n-3] + ((4*h)/3)*((2 * f(x[n-2],y[n-2])) - f(x[n-1],y[n-1]) + (2 * f(x[n],y[n]))) 
yc = y[n-1] + (h/3)*(f(x[n-1],y[n-1]) + (4 * f(x[n],y[n])) + f(x[n] + h,yp)) 
print("predtor : " ,yp)
print("correction : ", yc)
