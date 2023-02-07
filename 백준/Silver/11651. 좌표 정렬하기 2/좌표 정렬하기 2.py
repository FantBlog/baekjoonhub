import sys
n = int(sys.stdin.readline())
result = list()
for _ in range(n):
    result.append(list(map(int,sys.stdin.readline().split())))
result.sort(key=lambda x:(x[1],x[0]))
for i in range(n):
    print(*result[i])