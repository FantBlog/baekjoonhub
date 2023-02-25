import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(20_000)

def DFS(now):
    global cnt
    result = False
    for next in nodes[now]:
        if next != cut:
            que.append(next)
            cnt += 1
            result = True
    if result: # 자식이 있다면
        cnt -= 1


N = int(input())
nums = list(map(int,input().split()))
cut = int(input())

que = deque()
cnt = 1

nodes = [[] for _ in range(N+1)]
for child, parent in enumerate(nums):
    if parent == -1:
        master = child
        continue
    nodes[parent].append(child)

nodes[cut].clear()

if cut == master:
    print(0)
    exit()

que.append(master)

while que:
    DFS(que.popleft())

print(cnt)