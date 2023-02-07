from collections import deque
import sys
input = sys.stdin.readline
k = int(input())
a = deque()
for _ in range(k):
    t = int(input())
    if t == 0:
        a.pop()
    else:
        a.append(t)
print(sum(a))