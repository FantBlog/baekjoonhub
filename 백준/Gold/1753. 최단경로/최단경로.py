import sys
import heapq
def input(): return sys.stdin.readline().rstrip()

N, M = map(int,input().split())
START = int(input())

graph = [dict() for _ in range((N+1))]
node = [float('inf')] * (N+1)
que = []
vis = set()

for _ in range(M):
    start, end, cost = map(int,input().split())
    if graph[start].get(end):
        graph[start][end] = min(cost,graph[start].get(end))
    else:
        graph[start][end] = cost

que.append((0,START))
node[START] = 0

while que:
    now_cost, now_node = heapq.heappop(que)

    if now_cost > node[now_node]:
        continue

    else:
        for nextnum, nextcost in graph[now_node].items():
            distance = nextcost + now_cost
            
            if node[nextnum] > distance:
                node[nextnum] = distance
                heapq.heappush(que, (distance, nextnum))

for end in range(1,N+1):
    print(node[end] if node[end] != float('inf') else 'INF')