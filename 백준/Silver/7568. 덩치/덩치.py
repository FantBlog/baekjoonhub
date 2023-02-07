n = int(input())
dunk = []
for _ in range(n):
    dunk.append(tuple(map(int,input().split())))
result = []
for i in range(n):
    count = 1
    for j in range(n):
        if j != i:
            if dunk[j][0] > dunk[i][0] and dunk[j][1] > dunk[i][1]:
                count += 1
    result.append(count)

print(*result)