import sys
from collections import deque
input = sys.stdin.readline

def subin(n):
    if som.get(n+1) == None and 0 <= n+1 <= 100000:
        som[n+1] = som.get(n) + 1
        point.append(n+1)
    
    if som.get(n-1) == None and 0 <= n-1 <= 100000:
        som[n-1] = som.get(n)+ 1
        point.append(n-1)

    if som.get(n*2) == None and 0 <= n*2 <= 100000:
        som[n*2] = som.get(n)+ 1
        point.append(n*2)

som = {}
n,k = map(int,input().split())
som[n] = 0
point = deque()
point.append(n)

while som.get(k) == None:
    subin(point.popleft())
print(som.get(k))