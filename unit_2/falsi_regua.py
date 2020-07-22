from math import cos, exp

expression = "exp(x)-(5*cos(x))-1"
approx = 6

def f(x):
    return eval(expression)

def getSign(x):
    if(x > 0):
        return 1
    if(x < 0):
        return -1
    if(x == 0):
        return 0

def getInitial():
    i = 0
    s = getSign(f(i))
    print("f("+str(i)+") =",f(i))
    for i in range(1,5):
        print("f("+str(i)+") =",f(i))
        if(getSign(f(i)) == s):
            s = getSign(f(i))
            continue
        else:
            return i-1,i
    i = 0
    s = getSign(f(i))
    for i in range(-1,-5,-1):
        print("f("+str(i)+") =",f(i))
        if(getSign(f(i)) == s):
            s = getSign(f(i))
            continue
        else:
            return i,i+1

def bisection(left,right,approx):
    sl = getSign(f(left))
    sr = getSign(f(right))
    print((right - left) > (0.000001))
    i = 0
    while (right - left > (10**(-1 * approx)) and i < 10):
        i += 1
        mid = ((left * f(right)) - (right * f(left))) / ((f(right) - f(left)))
        print("================")
        print("left",left,"mid",mid,"right",right)
        print("f(left)",f(left))
        print("f(mid)",f(mid))
        print("f(right)",f(right))
        sm = getSign(f(mid))
        if(sm == 0 or (mid - left < (10**(-1 * approx))) or (right - mid < (10**(-1 * approx)))):
            return mid
        elif(sm == sl):
            left = mid
        elif(sm == sr):
            right = mid
    
    return left

i1,i2 = getInitial()
print("roots between",i1,"and",i2)
root = bisection(i1,i2,approx)
print("root approximated to",approx,"decimal is",root)
