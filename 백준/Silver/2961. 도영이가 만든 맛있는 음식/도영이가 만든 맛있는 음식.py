import sys
input = sys.stdin.readline

n = int(input())
jae = []
for i in range(n):
    jae.append(tuple(map(int,input().split())))

mat = 1000000000
for i in range(1,1<<n):
    sin = 1
    ssn = 0
    for j in range(n):
        if i & (1<<j):
            sin *= jae[j][0]
            ssn += jae[j][1]
    total = abs(sin-ssn)
    if total < mat:
        mat = total
print(mat)