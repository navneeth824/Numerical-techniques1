import sys, os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from print_matrix import printA,printArr
from fractions import Fraction

def solveUpper(n,U,B):
    sol = [0] * n
    for y in range(n-1, -1, -1):
        extra = 0
        for x in range(y+1,n):
            extra = extra + (U[y][x] * sol[x])
        sol[y] = (B[y] - extra) / U[y][y]
    return sol

def solveLower(n,L,B):
    sol = [0] * n
    for y in range(n):
        extra = 0
        for x in range(y):
            extra =  extra + (L[y][x] * sol[x])
        sol[y] = (B[y] - extra) / L[y][y]
    return sol

def crout(n,A):
    L = [[0 for i in range(n)] for i in range(n)]
    U = [[0 for i in range(n)] for i in range(n)]
    print("n :",n)
    for y in range(n):
        for x in range(n):
            if x <= y: # set L
                sub = 0
                for i in range(x):
                    sub = sub + (L[y][i] * U[i][x])
                L[y][x] = A[y][x] - sub
                L[y][x] = Fraction(L[y][x]).limit_denominator() # to display the metrix as fraction
                print("L",y,x,"=",Fraction(L[y][x]).limit_denominator())
                if x == y:
                    U[y][x] = 1
                    print("U",y,x,"=",Fraction(U[y][x]).limit_denominator())
            else: # set U
                sub = 0
                for i in range(y):
                    sub = sub + (L[y][i] * U[i][x])
                U[y][x] = (A[y][x] - sub) / L[y][y]
                print("U",y,x,"=",Fraction(U[y][x]).limit_denominator())    
    return L,U


if __name__ == "__main__":
    A = [
        [5,1,3],
        [4,-3,1],
        [3,-2,-1]
    ]
    B = [10,18,11]
    n = len(A)
    L,U = crout(n,A)
    print()
    print("L :")
    printA(L)
    print("U :")
    printA(U)

    Y = solveLower(n,L,B)
    print("Y :",end=" ")
    printArr(Y)
    X = solveUpper(n,U,Y)
    print("X :",end=" ")
    printArr(X)
