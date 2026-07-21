#Matrix Multiplication

rows = 2
cols = 2

print("Enter Matrix A")

A = []

for i in range(rows):
    row = list(map(int, input().split()))
    A.append(row)

print("Enter Matrix B")

B = []

for i in range(rows):
    row = list(map(int, input().split()))
    B.append(row)

result = [[0, 0], [0, 0]]

for i in range(rows):
    for j in range(cols):
        for k in range(cols):
            result[i][j] += A[i][k] * B[k][j]

print("Result Matrix:")

for row in result:
    print(row)