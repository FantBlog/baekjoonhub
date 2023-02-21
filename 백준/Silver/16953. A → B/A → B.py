from collections import deque

A, B = map(int,input().split())

que = deque()
que.append(A)

vis = dict()
vis[A] = 1

Find = True

if A == B:
    print(1)
    exit()

while Find:
    if not que or min(que) > B:
        print(-1)
        exit()

    for _ in range(len(que)):
        num = que.popleft()

        if num*2 <= int(10**9):
            vis[num*2] = vis[num] + 1

            que.append(num*2)

            if num*2 == B:
                Find = False
                break 

        if num*10+1 <= int(10**9):
            vis[num*10+1] = vis[num] + 1

            que.append(num*10 + 1)
            
            if num*10 + 1 == B:
                Find = False
                break
print(vis[B])