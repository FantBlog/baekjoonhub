import sys
n , k = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))
temp = total = sum(lst[:k])
o = 0
p = k
for i in range(k,n):
    temp += lst[p]-lst[o]
    p += 1
    o += 1
    if total < temp:
        total = temp
print(total)