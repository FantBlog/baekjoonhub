from collections import deque
import sys
n = int(input())
q = deque()
for _ in range(n):
    order = sys.stdin.readline()
    if order[:2] == 'pu':
        if order[:6] == 'push_b':
            od,x = order.split()
            q.append(int(x))
        else:
            od,x = order.split()
            q.appendleft(int(x))
    elif order[:2] == 'po':
        if order[:5] == 'pop_b':
            try:
                print(q.pop())
            except:
                print('-1')
        else:
            try:
                print(q.popleft())
            except:
                print('-1')
    elif order[:2] == 'si':
        print(len(q))
    elif order[:2] == 'em':
        if len(q):
            print('0')
        else:
            print('1')
    elif order[:2] == 'fr':
        try:
            print(q[0])
        except:
            print('-1')
    elif order[:2] == 'ba':
        try:
            print(q[-1])
        except:
            print('-1')