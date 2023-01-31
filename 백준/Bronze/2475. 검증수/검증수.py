t = list(map(int,input().split()))
print(sum([i**2 for i in t])%10)