from math import ceil, fabs
coeff = [1,-14,78,-176,136]
m = 3
n = len(coeff)
for i in range(m):
    print(coeff)
    print("--------------------")
    c = []
    for j in range(ceil(n/2)):
        cj = []
        for k in range(n):
            cj.append(0)
            if j == 0:
                d = 1
            else:
                d = ((-1)**j) * 2
            # print("d : ",d)
            if k-j >= 0 and k+j < n:
                cj[k] = coeff[k-j]*coeff[k+j]*d

        print(cj)
        c.append(cj)
    
    print("--------------------")
    for j in range(n):
        coeff[j] = 0
        for k in range(ceil(n/2)):
            coeff[j] = coeff[j] + c[k][j]
print(coeff,end="\n\n")

for i in range(1,n):
    bm = fabs(coeff[i]/coeff[i-1])
    print("| b",i, "/ b", (i-1), "| =", bm, end="\t")
    print(2**m, "th root = ", bm**(1/(2**m)))        


