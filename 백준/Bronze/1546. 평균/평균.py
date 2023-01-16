nm = int(input())
lst = list(map(int,input().split()))
idx = 0
mx = max(lst)
for i in lst:
    lst[idx] = i / mx * 100
    idx +=1
print(sum(lst)/nm)