n = 100
result = [[0 for _ in range(n)] for _ in range(n)]
t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    for i in range(10):
        for j in range(10):
            result[x + i][y + j] = 1
count = 0
for i in range(n):
    for j in range(n):
        if result[i][j]:
            count += 1
print(count)