import sys
input = sys.stdin.readline
n, m = map(int,input().split())
first = []
for _ in range(n):
    first.append(list(map(int,input().split())))
k = int(input())
for _ in range(k):
    i, j, x, y = map(int,input().split())
    i -= 1
    j -= 1
    total = 0
    for o in range(i,x):
        total += sum(first[o][j:y])
    print(total)