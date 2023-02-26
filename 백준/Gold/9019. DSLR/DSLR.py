from collections import deque

def BFS(num, order):
    if num == end:
        return order
    
    D = num*2%10_000
    if vis[D] == float('inf'):
        que.append((D, order+1))
        vis[D] = order + 1
    
    S = num - 1
    if S < 0:
        S = 9999
    if vis[S] == float('inf'):
        que.append((S,order + 1))
        vis[S] = order + 1
    
    a,b = divmod(num * 10 , 10_000)
    L = b+a
    if vis[L] == float('inf'):
        que.append((L,order + 1))
        vis[L] = order + 1

    a,b = divmod(num, 10)
    R = b*1000 + a
    if vis[R] == float('inf'):
        que.append((R,order + 1))
        vis[R] = order + 1
    

def reverse_BFS(num, order):
    if num == start:
        return True
    
    if num % 2 == 0:
        D = (num+10_000) // 2
        if vis[D] == order - 1:
            que.append((D, order - 1))
            result.appendleft('D')
            return
        D = num // 2
        if vis[D] == order - 1:
            que.append((D, order - 1))
            result.appendleft('D')
            return
    
    S = num + 1
    if S == 10000:
        S = 0
    if vis[S] == order - 1:
        que.append((S,order - 1))
        result.appendleft('S')
        return
    
    a,b = divmod(num, 10)
    L = b*1000 + a
    if vis[L] == order - 1:
        que.append((L,order - 1))
        result.appendleft('L')
        return

    a,b = divmod(num * 10 , 10_000)
    R = b+a
    if vis[R] == order - 1:
        que.append((R,order - 1))
        result.appendleft('R')
        return


for _ in range(int(input())):
    start, end = map(int,input().split())
    que = deque()
    que.append((start,0))
    vis = [float('inf')] * 10001
    vis[start] = 0

    while que:
        order = BFS(*que.popleft())
        if order:
            que.clear()
            break
    
    result = deque()
    que.append((end,order))

    while que:
        if reverse_BFS(*que.popleft()):
            print(*result,sep='')
            break