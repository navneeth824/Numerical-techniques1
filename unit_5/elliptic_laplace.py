grid = [                       # initial grid
    [0 , 1 , 2 , 0],
    [1 , 0 , 0 , 2],
    [2 , 0 , 0 , 1],
    [0 , 2 , 1 , 0]
]
h = 1
n = 4  # number of iterations

for i in range(n):
    print("iterration",i,"\n===========")
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            grid[x][y] = (grid[x][y-1] + grid[x-1][y] + grid[x][y+1] + grid[x+1][y])/4
            print("u",x,",",y,"=",grid[x][y])
    print("\n===========\n")
