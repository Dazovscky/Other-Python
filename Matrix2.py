rows = int(input())
cols = int(input())
matrix = []
list = []
for r in range(rows):
    for c in range(cols):
        word = input()
        list.append(word)

    matrix.append(list)
    list = []

for r in range(rows):
    for c in range(cols):
        print(matrix[r][c], end=' ')
    print()
print()
for c in range(cols):
    for r in range(rows):
        print(matrix[r][c], end=' ')
    print()