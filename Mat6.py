n = int(input())
matrix = [[0]*n for _ in range(n)]    # создаем квадратную матрицу размером 8×8

for i in range(n): # заполняем главную диагональ единицами, а побочную двойками
    matrix[i][n-i-1] = 1
    for j in range(n):
        if i > j:
            if i + j + 2:
                matrix[n-j-1][i] = 2

for r in range(n):                     # выводим матрицу
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()