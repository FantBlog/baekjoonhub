import sys
import heapq
from collections import deque
def input(): return sys.stdin.readline().rstrip()

N = int(input())
M = int(input())

graph = [[] for _ in range((N+1))]
node = [float('inf')] * (N+1)
que = []
vis = set()

for _ in range(M):
    start, end, cost = map(int,input().split())
    graph[start].append((end,cost))

start, end = map(int,input().split())

if start == end:
    print(0)
    exit()

que.append((start,0))
node[start] = 0

while que:
    now_node, now_cost = heapq.heappop(que)

    if now_cost > node[now_node]:
        continue

    else:
        for nextnum, nextcost in graph[now_node]:
            distance = nextcost + now_cost
            if node[nextnum] > distance:
                node[nextnum] = distance
                heapq.heappush(que, [nextnum, distance])

print(node[end])