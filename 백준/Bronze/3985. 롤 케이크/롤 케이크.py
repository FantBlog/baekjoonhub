L = int(input())
N = int(input())
arr = [-1] * (L+1)
res1 = 0
mx1 = 0
res2 = 0
mx2 = 0
for i in range(1,1+N):
    a, b = map(int,input().split())
    if b - a > mx2:
        mx2 = b - a
        res2 = i
    for j in range(a,b+1):
        if arr[j] == -1:
            arr[j] = i
for i in range(1,N+1):
    if mx1 < arr.count(i):
        mx1 = arr.count(i)
        res1 = i
print(res2)
print(res1)