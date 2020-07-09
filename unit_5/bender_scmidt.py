import sys, os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from print_matrix import printIndexed

ux0 = "x*(4-x)"     # f(x)
def f(x):
    return eval(ux0)

u0t = "0"     
def T0(t):
    return eval(u0t)

ult = "0"     
def Tl(t):
    return eval(ult)

def benderSchmidth(l,h,k,endT):
    nx = int((l/h) + 1)
    nt = int((endT/k) + 1)
    U = [[0 for i in range(nx)] for j in range(nt)]
    for t in range(nt):
        U[t][0] = T0(t*k)
    for t in range(nt):
        U[t][nx-1] = Tl(t*k)
    for x in range(nx):
        U[0][x] = f(x*h)
    
    for t in range(1,nt):
        for x in range(1,nx-1):
            U[t][x] = (U[t-1][x-1] + U[t-1][x+1])/2
    printIndexed(U,h,k)

if __name__ == "__main__":
    l = 4
    h = 1
    a = 2
    endT = 5
    k = (a*(h**2))/2
    benderSchmidth(l, h, k, endT)
