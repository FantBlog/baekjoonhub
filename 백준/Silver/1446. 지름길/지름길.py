N, D = map(int, input().split())

graph = dict()
dp = [D for _ in range(D + 1)]

for _ in range(N):
    s, e, t = map(int, input().split())
    
    if t > e - s or e > D:
        continue
    graph.setdefault(s, list())
    graph[s].append((e, t))


for i in range(D + 1):
    if i == 0:
        dp[i] = 0
    else:
        dp[i] = min(dp[i], dp[i - 1] + 1)

    if graph.get(i) == None:
        continue

    for e, t in graph[i]:
        dp[e] = min(dp[e], dp[i] + t)

print(dp[D])