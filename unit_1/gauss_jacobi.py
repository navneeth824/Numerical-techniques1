import sys, os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from print_matrix import printArr

def gaussJacobi(AB):
    n = 6    # number of iterations
    o = len(AB)
    sol = [0]* o
    for i in range(n):
        tempsol = sol.copy()
        print("iteration :",i+1)
        for j in range(o):
            sub =  0
            for k in range(o):
                if k == j:
                    continue
                sub = sub + (AB[j][k] * tempsol[k])
            sol[j] = (AB[j][o] - sub)/AB[j][j]
            print("sol",j,"=",sol[j])
    return sol

if __name__ == "__main__":
    AB = [           # enter in diagnal dominant manner
        [20,2,1,104],
        [5,25,3,56],
        [6,2,30,92]
    ]

    X = gaussJacobi(AB)
    print("solution :")
    printArr(X)
