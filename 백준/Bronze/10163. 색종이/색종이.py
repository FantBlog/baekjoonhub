t = int(input())
n = 1001
result = [[0 for _ in range(n)] for _ in range(n)]
for paper in range(1,t+1):
    x,y,c,r = map(int,input().split())
    for i in range(c):
        for j in range(r):
            result[x + i][y + j] = paper
for paper in range(1,t+1):
    count = 0
    for i in range(n):
        for j in range(n):
            if result[i][j] == paper:
                count += 1
    print(count)