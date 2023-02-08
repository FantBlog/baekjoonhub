tile = [1,1,2]
n = int(input())
for i in range(2,n+1):
    if len(tile) <= i:
        tile.append(tile[i-1]+tile[i-2])
print(tile[n]%10007)