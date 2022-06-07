num = str(input()).split()
n, m = int(num[0]), int(num[1])
matrix = [['.']*m for _ in range(n)]
step = "*"
for cc in range(n):
    for rr in range(m):

        if cc % 2 == 1 and rr % 2 == 0:
            matrix[cc][rr] = step
        elif cc % 2 == 0 and rr % 2 ==1:
            matrix[cc][rr] = step
        print(matrix[cc][rr], end='  ')
    print()
print()