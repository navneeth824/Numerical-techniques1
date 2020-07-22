c = [1,0,-6,-18]

def f(x):
    res = 0
    deg = len(c) - 1
    for i in range(deg + 1):
        res += c[i]*(x**(deg - i))
    return res

def getSign(x):
    if(x > 0):
        return 1
    if(x < 0):
        return -1
    if(x == 0):
        return 0

def getFloorRoot():
    print("\nfinding the root range")
    i = 0
    s = getSign(f(i))
    for i in range(1,10):
        if(getSign(f(i)) == s):
            s = getSign(f(i))
            continue
        else:
            print("f("+str(i-1)+") =",f(i-1))
            print("f("+str(i)+") =",f(i))
            print("sig digit :",i-1)
            return i-1
    print("f("+str(9)+") =",f(9))
    print("f("+str(10)+") =",f(10))
    print("sig digit :",9)
    return 9

def divide(x):
    print("\ndividing it by",x)
    for i in range(0,len(c)-1):
        print(c)
        add = [0]
        for j in range(1,len(c)-i):
            add.append(x*c[j-1])
            c[j] += add[j]
        print(add)
        print("----------------")
    print(c)

def raiseroot():
    print("\nraising the roots")
    for i in range(len(c)):
        c[i] *= 10**i
    print(c)

def horner():
    n = 2     # number of decimal
    r = getFloorRoot()
    sol = r
    for i in range(1,n+1):
        divide(r)
        raiseroot()
        r = getFloorRoot()
        sol += r * (10**((-1)*i))
    
    print("answer correct to",n,"decimal places is",sol)

horner()
