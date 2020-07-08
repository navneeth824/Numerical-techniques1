import sys, os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from fractions import Fraction
from print_matrix import printArr

def checkSign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    if x == 0:
        return 0

def multiply(A,B):    # multiply n*n matrix by n*1 matrix
    n = len(A)
    sol = [0] * n
    for y in range(n):
        for x in range(n):
            sol[y] = sol[y] + (A[y][x] * B[x])
    return sol

def extractMax(B,sign = 0):
    maxB = max(B,key=abs)
    if sign != 0 and sign != checkSign(maxB):
        maxB = -maxB
    sol = []
    for b in B:
        b = Fraction(b/maxB).limit_denominator()
        sol.append(b)
    return maxB,sol

def dominantEigen(A,B = [1,0,0]):
    n = 4 # number of iterations
    E = 0
    for i in range(n):
        print("iteration :",i+1)
        B = multiply(A,B)
        E,B = extractMax(B,checkSign(E))
        print("eigen value:",E)
        print("eigen vector:")
        printArr(B)

if __name__ == "__main__":
    A = [
        [3,-1,1],
        [-1,5,-1],
        [1,-1,3]
    ]
    dominantEigen(A)
