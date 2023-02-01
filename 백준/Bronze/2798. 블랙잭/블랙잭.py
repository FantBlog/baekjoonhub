n,m = map(int,input().split())
card = list(map(int,input().split()))
result = []
for i in range(n-2):
    for j in range(i+1,n-1):
        for h in range(j+1,n):
            total = card[i]+card[j]+card[h]
            if total <= m:
                result.append(total)
print(max(result))