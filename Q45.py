l = []
for i in range(0,2):
    a = []
    for j in range(0,2):
        a.append(int(input()))
    l.append(a)
for i in range(0,2):
    for j in range(0,2):
        print(l[i][j],end = " ")
    print()


