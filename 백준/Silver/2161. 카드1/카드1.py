from collections import deque
import sys
n = int(sys.stdin.readline())
dq = deque(i for i in range(1,n+1))
result = deque()
for _ in range(n-1):
    result.append(dq.popleft())
    dq.append(dq.popleft())
print(*result,dq[0])