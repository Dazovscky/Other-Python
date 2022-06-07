n = int(input())
arr = []
mtr = [[int(i) for i in input().split()] for j in range(n)]
for i in range(n):
    for j in range(n):
        if i >= j:
            arr.append(mtr[i][j])
print(max(arr))