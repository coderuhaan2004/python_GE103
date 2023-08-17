mat1 = [[int(input())for x in range(0,2)] for y in range(0,2)]
mat2 = [[int(input())for x in range(0,2)] for y in range(0,2)]
mat3 = []

for i in range(0,2):
    mat3.append([mat1[i][j]+mat2[i][j] for j in range(0,2)])
for i in range(0,2):
    for j in range(0,2):
        print(mat3[i][j], end = " ")
    print()

        







