from collections import deque
n, k = map(int,input().split())
q = deque(i for i in range(1,n+1))

print('<',end='')
for i in range(1,n * k + 1):
    if i % k:
        q.append(q.popleft())
    else:
        if i == n * k:
            print(q.popleft(),end='>')
        else:
            print(q.popleft(),end=', ')