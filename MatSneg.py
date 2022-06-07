n = int(input())
matrix = [['.'] * n for _ in range(n)]
star = '*'

for rows in range(n):
    for colum in range(n):
        if rows <= rows+1 and colum == rows:
            matrix[rows][colum] = star
            matrix[rows][n - rows - 1] = star
            matrix[rows][n // 2] = star
            matrix[n // 2][colum] = star


for r in range(n):
    # выводим матрицу
    for c in range(n):
        print(matrix[r][c], end='  ')
    print()