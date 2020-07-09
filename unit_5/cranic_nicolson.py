import sys, os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from print_matrix import printIndexed
from unit_1.gauss_jordan import gaussJordan

ux0 = "0"     # f(x)
def f(x):
    return eval(ux0)

u0t = "0"     
def T0(t):
    return eval(u0t)

ult = "t"     
def Tl(t):
    return eval(ult)

def getEquation(x,t,lam,U):
    Ai = [0]*(len(U[0]) - 1)
    c = lam*(U[t-1][x-1]+U[t-1][x+1]) - (2*(lam-1)*U[t-1][x])
    Ai[x-1] = 2*(lam + 1)
    # left
    if x == 1:
        c += lam*U[t][x-1]
    else:
        Ai[x-2] = -lam
    # right
    if x == len(U[0]) - 2:
        c += lam*U[t][x+1]
    else:
        Ai[x] = -lam
    
    Ai[len(U[0]) - 2] = c
    return Ai

def cranicNicolson(l, h, k, endT, lam):
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
        A = []
        for x in range(1,nx-1):
            A.append(getEquation(x,t,lam,U))
        print("\nusing gauss jordan to solve for t = ",t*k,"\n")
        ut = gaussJordan(len(A),A)
        for x in range(1,nx-1):
            U[t][x] = ut[x-1]

    print("the final table is : \n")
    printIndexed(U,h,k)
    return U

if __name__ == "__main__":
    l = 1
    h = 1/4
    a = 1
    endT = 1/4
    k = 1/8
    lam  = k/(a*(h**2))
    cranicNicolson(l,h, k, endT,lam)
