n,gij=map(int,input().split())
lst = list(map(int,input().split()))
result = []
for i in lst:
    if i < gij:
        result.append(i)
for i in result:
    print(i, end=" ")