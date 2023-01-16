t=int(input())
lst = list(map(int,input().split()))
res = []
for i in range(201):
    res.append(0)
for idx in lst:
    res[idx+100] += 1
b = int(input())
print(res[b+100])