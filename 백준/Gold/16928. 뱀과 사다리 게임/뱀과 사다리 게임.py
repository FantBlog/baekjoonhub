from collections import deque
n, m = map(int,input().split())
up_portal = dict()
down_portal = dict()
for _ in range(n):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    up_portal[a] = b
for _ in range(m):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    down_portal[a] = b

dp = [99] * 100 # 1번 부터 100 번 까지 0~99
visit = [0] * 100 # 1번 부터 100 번 까지 0~99
dp[0] = 0
end = True
start = deque()
start.append(0)
while len(start) > 0:
    now = start.popleft()
    if visit[now]:
        continue
    if up_portal.get(now):
        dp[up_portal[now]] = min(dp[now],dp[up_portal[now]])
        if end:
            start.append(up_portal[now])
    elif down_portal.get(now):
        dp[down_portal[now]] = min(dp[now],dp[down_portal[now]])
        if end:
            start.append(down_portal[now])
    else:
        for i in range(1,7):
            if now+i < 100 and now+i == 99:
                dp[now+i] =  min(dp[now] + 1, dp[now+i])
                end = False
                
            if now+i < 100 and dp[now+i] == 99:
                dp[now+i] = min(dp[now] + 1, dp[now+i])
                if up_portal.get(now+i):
                    dp[up_portal[now+i]] = min(dp[now] + 1,dp[up_portal[now+i]])
                    if end:
                        start.append(up_portal[now+i])
                elif down_portal.get(now+i):
                    dp[down_portal[now+i]] = min(dp[now] + 1,dp[down_portal[now+i]])
                    if end:
                        start.append(down_portal[now+i])
                else:
                    if end:
                        start.append(now+i)
    visit[now] = 1

print(dp[99])