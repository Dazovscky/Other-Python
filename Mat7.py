numb = str(input()).split()
n = numb[0]
m = numb[1]
matrix = [[0]*int(m) for _ in range(int(n))]
temp = 0

def print_matrix(matrix, n):
    for r in range(int(n)):
        for c in range(int(m)):
            print(str(matrix[r][c]).ljust(3), end='  ')
        print()


for i in range(int(n)):

    for j in range(int(m)):
        temp += 1
        matrix[i][j] = temp

print_matrix(matrix, n)