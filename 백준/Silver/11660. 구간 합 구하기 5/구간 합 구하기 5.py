import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
for x in range(n):
    for y in range(n):
        if x == 0 and y == 0:
            continue
        elif x == 0:
            arr[x][y] += arr[x][y-1]
        elif y == 0:
            arr[x][y] += arr[x-1][y]
        else:
            arr[x][y] += arr[x-1][y] + arr[x][y-1] - arr[x-1][y-1]

for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1
    if x1 == 0 and y1 == 0:
        total = arr[x2][y2]
    elif x1 == 0:
        total = arr[x2][y2] - arr[x2][y1-1]
    elif y1 == 0:
        total = arr[x2][y2] - arr[x1-1][y2]
    else:
        total = arr[x2][y2] - arr[x2][y1-1] - arr[x1-1][y2] + arr[x1-1][y1-1]
    print(total)