import sys
input = sys.stdin.readline
n, k = map(int,input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)
result = 0
for i in range(n):
    if coin[i] <= k:
        result += k // coin[i]
        k %= coin[i]
print(result)