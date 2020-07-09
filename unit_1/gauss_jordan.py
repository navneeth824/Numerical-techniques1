import sys, os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from fractions import Fraction
from print_matrix import printAB, printArr

def gaussJordan(n,matrix):
    sol = []
    print("matrix : ")
    printAB(matrix)
    for x in range(n):
        print("==========")
        print("fixing a",x+1)
        for y in range(n):
            if x == y or matrix[y][x] == 0:
                continue
            axy = matrix[y][x]
            axx = matrix[x][x]
            print("transformation :","R",y,"->",axx,"*R"+str(y),"-",axy,"*R"+str(x))
            for z in range(n+1):
                matrix[y][z] = Fraction((axx * matrix[y][z]) - (axy * matrix[x][z])).limit_denominator()
        printAB(matrix)
    for y in range(n):
        sol.append(matrix[y][n] / matrix[y][y])
    print("solution :")
    printArr(sol)
    return sol

if __name__ == "__main__":
    matrix = [
        [1,4,9,16],
        [2,1,1,10],
        [3,2,3,18]
    ]
    n = len(matrix)
    sol = gaussJordan(n,matrix)
