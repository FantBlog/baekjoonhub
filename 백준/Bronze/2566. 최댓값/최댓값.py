a = [list(map(int, input().split())) for _ in range(9)]
m = 0
ci = cj = 1
for i in range(9):
    for j in range(9):
        if a[i][j] > m:
            m = a[i][j]
            ci = i + 1
            cj = j + 1
print(m)
print(ci, cj)