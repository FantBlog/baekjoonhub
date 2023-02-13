import sys
input = sys.stdin.readline
from collections import deque

text = input().rstrip('\n')
front = deque()
back = deque()
top = -1
for txt in text:
    top += 1
    front.append(txt)

n = int(input().rstrip('\n'))
for _ in range(n):
    order = list(input().rstrip('\n'))
    if order[0] == 'L':
        if len(front):
            back.appendleft(front.pop())
    elif order[0] == 'D':
        if len(back):
            front.append(back.popleft())
    elif order[0] == 'B':
        if len(front):
            front.pop()
    else:
        if len(front) + len(back) < 600000:
            front.append(order[-1])
print(*front,*back,sep='')