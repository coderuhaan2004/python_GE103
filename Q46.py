# Input for the first matrix
mat1 = [[int(input()) for i in range(0, 2)] for j in range(0, 2)]

# Input for the second matrix
mat2 = [[int(input()) for i in range(0, 2)] for j in range(0, 2)]

# Initialize the result matrix mat3
mat3 = [[0, 0], [0, 0]]

# Perform matrix multiplication
for i in range(0, 2):
    for j in range(0, 2):
        for k in range(0, 2):
            mat3[i][j] += mat1[i][k] * mat2[k][j]

# Print the result matrix mat3
for i in range(0, 2):
    for j in range(0, 2):
        print(mat3[i][j])

