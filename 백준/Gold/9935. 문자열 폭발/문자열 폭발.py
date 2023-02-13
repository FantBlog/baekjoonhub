import sys
from collections import deque
input = sys.stdin.readline
text = input().rstrip('\n')
boom = input().rstrip('\n')
bmm = deque()
bm = deque()
for b in boom:
    bm.append(b)
for txt in text:
    bmm.append(txt)
    if txt == bm[-1] and len(bmm) >= len(boom):
        if all(bmm[-i] == bm[-i] for i in range(1,len(boom)+1)):
            for _ in range(len(boom)):
                bmm.pop()

if len(bmm):
    print(*bmm,sep='')
else:
    print('FRULA')