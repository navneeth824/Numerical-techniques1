import sys, os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from print_matrix import printIndexed

exp1 = "x*(4-x)"


def ux0(x):
    return eval(exp1)


exp2 = "0"  # u(0,t) and u(l,t)


def u0t(t):
    return eval(exp2)


def hyperbolic(a, l, h, k, T):
    nx = int((l / h) + 1)
    nt = int((T / k) + 1)
    U = [[0 for i in range(nx)] for j in range(nt)]
    for t in range(nt):
        U[t][0] = u0t(t * k)
        U[t][nx - 1] = u0t(t * k)
    # first row
    for x in range(nx):
        U[0][x] = ux0(x * h)
    # second row
    for x in range(1, nx - 1):
        U[1][x] = (U[0][x - 1] + U[0][x + 1]) / 2
    
    # remaining rows
    for t in range(2,nt):
        for x in range(1,nx-1):
            U[t][x] = U[t-1][x-1] + U[t-1][x+1] - U[t-2][x]
    
    printIndexed(U,h,k)

if __name__ == "__main__":
    a = 2  # alpha
    l = 4  # length
    h = 1
    k = h / a
    T = 2  # till what time do you need
    hyperbolic(a, l, h, k, T)
