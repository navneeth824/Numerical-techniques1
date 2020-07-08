from pandas import DataFrame
import fractions

def printAB(m):
    col = ["a"+str(i+1) for i in range(len(m))]
    col.append("b")
    ind = [""] * len(m)
    print(DataFrame(m,index=ind,columns=col),end="\n\n")

def printA(m):
    col = ["a"+str(i+1) for i in range(len(m))]
    ind = [""] * len(m)
    df = DataFrame(m,index=ind,columns=col)
    print(df,end="\n\n")

def printArr(a):
    col = [""]
    ind = [""] * len(a)
    df = DataFrame(a,index=ind,columns=col)
    print(df,end="\n\n")
