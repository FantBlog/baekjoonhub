import sys
input = sys.stdin.readline

n = int(input())
km = list(map(int,input().split()))
won = list(map(int,input().split()))

if n == 2:
    print(won[0]*km[0])
    exit()

start_won = won[0]
start_km = km[0]
km = km[1:]
won = won[1:n-1]
total = start_won * start_km
while True:
    idx = won.index(min(won))
    if idx == 0:
        total += won[0] * sum(km)
        break
    else:
        total += won[idx] * sum(km[idx:])
        n = idx

print(total)