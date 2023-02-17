import sys
from collections import deque
n = int(sys.stdin.readline())
que = deque()
for _ in range(n):
    order = sys.stdin.readline()

    if order[:2] == 'pu': # 푸시
        od,x = order.split()
        que.append(x)

    elif order[:2] == 'po': # 팝
        if len(que):
            print(que.popleft())
        else:
            print('-1')

    elif order[:2] == 'si': # 사이즈
        print(len(que))

    elif order[:2] == 'em': # 비어있냐
        if len(que):
            print('0')
        else:
            print('1')

    elif order[:2] == 'fr': # 맨앞
        if len(que):
            print(que[0])
        else:
            print('-1')

    else:
        if len(que):
            print(que[-1])
        else:
            print('-1')