c = [1,1,-16,20]

for i in range(3):
    print(c)
    print("--------------------")
    c1 = []
    c2 = [0,0,0,0]
    c2[1] = -2 * c[0] * c[2]
    c2[2] = -2 * c[1] * c[3]
    for co in c:
        c1.append(co*co)
    print(c1)
    print(c2)
    print("--------------------")
    for j in range(4):
        c[j] = c1[j]+c2[j]

print(c)


