n,m = map(int,input().split())
last = []
for i in range(1<<n):
    result = list()
    count = 0
    for j in range(n):
        if i & (1<<j):
            result.append(j+1)
            count += 1
    if count == m:
        last.append(result)
last.sort()
for i in last:
    print(*i,sep=' ')
