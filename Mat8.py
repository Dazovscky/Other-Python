n = int(input())
matrix = [[0] * n for _ in range(n)]
star = '1'

for rows in range(n):
    for colum in range(n):
        if rows <= rows+1 and colum == rows:
            matrix[rows][colum] = star
            matrix[rows][n - rows - 1] = star
        elif rows < colum and rows < n - 1 -colum:
            matrix[rows][colum] = star
        elif rows > colum and rows > n - 1 -colum:
            matrix[rows][colum] = star
for r in range(n):
    # выводим матрицу
    for c in range(n):
        print(matrix[r][c], end='  ')
    print()