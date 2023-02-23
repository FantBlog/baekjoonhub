import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

def subin(n):
    if 0 <= n+1 <= 100000:
        if som.get(n+1) == None:
            som[n+1] = [som.get(n)[0] + 1, 1]
            point.append(n+1)
        elif som[n+1][0] == som.get(n)[0]+1: # 가려는 곳이 왔던곳이랑 같다면
            som[n+1] = [som[n+1][0], som[n+1][1]+1]
            point.append(n+1)
    
    if 0 <= n-1 <= 100000:
        if som.get(n-1) == None:
            som[n-1] = [som.get(n)[0] + 1, 1]
            point.append(n-1)
        elif som[n-1][0] == som.get(n)[0]+1: # 가려는 곳이 왔던곳이랑 같다면
            som[n-1] = [som[n-1][0], som[n-1][1]+1]
            point.append(n-1)

    if 0 <= n*2 <= 100000:
        if som.get(n*2) == None:
            som[n*2] = [som.get(n)[0] + 1, 1]
            point.append(n*2)
        elif som[n*2][0] == som.get(n)[0]+1: # 가려는 곳이 왔던곳이랑 같다면
            som[n*2] = [som[n*2][0], som[n*2][1]+1]
            point.append(n*2)
    
som = {}
N, K = map(int,input().split())
som[N] = [0,1]
point = deque()
point.append(N)

while not som.get(K):
    for _ in range(len(point)):
        subin(point.popleft())
print(*som.get(K),sep='\n')