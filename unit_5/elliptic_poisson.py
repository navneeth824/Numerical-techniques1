import sys, os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from unit_1.gauss_jordan import gaussJordan

grid = [                       # initial grid
    [0 , 0 , 0 , 0],
    [0 , 0 , 0 , 0],
    [0 , 0 , 0 , 0],
    [0 , 0 , 0 , 0]
]
h = 1
exp = "-10*((x**2)+(y**2)+10)"
x = len(grid[0])
y = len(grid)

def f(xi,yi):
    return eval(exp,{'x':xi,'y':yi})

def ui(xi,yi):
    return (yi - 1)*(x-2) + (xi - 1)

def checkOnEdge(xi,yi):
    return xi == 0 or xi == x-1 or yi == 0 or yi == y-1

def getEquation(xi,yi,un):
    Ai = [0 for i in range(un+1)]
    Ai[un] = (h**2) * f(xi,y - yi - 1) # constant
    Ai[ui(xi,yi)] = -4
    print("xi :",xi,"yi :",yi)
    # top
    if checkOnEdge(xi,yi-1):
        Ai[un] -= grid[xi][yi-1]
    else:
        Ai[ui(xi,yi-1)] = 1
    # down
    if checkOnEdge(xi,yi+1):
        Ai[un] -= grid[xi][yi+1]
    else:
        Ai[ui(xi,yi+1)] = 1
    # left
    if checkOnEdge(xi-1,yi):
        Ai[un] -= grid[xi-1][yi]
    else:
        Ai[ui(xi-1,yi)] = 1
    # right
    if checkOnEdge(xi+1,yi):
        Ai[un] -= grid[xi+1][yi]
    else:
        Ai[ui(xi+1,yi)] = 1
    return Ai

def ellpticPoisson():
    un = (x - 2) * (y - 2)   # number of unknowns
    A = []
    for yi in range(1,y-1):
        for xi in range(1,x-1):
            A.append(getEquation(xi,yi,un))
    gaussJordan(un,A)


ellpticPoisson()

# print(f(1,1))
