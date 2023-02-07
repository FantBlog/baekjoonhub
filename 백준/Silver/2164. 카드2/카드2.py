from collections import deque
import sys
n = int(sys.stdin.readline())
dq = deque(i for i in range(1,n+1))
for _ in range(n-1):
    dq.popleft()
    dq.append(dq.popleft())
print(dq[0])