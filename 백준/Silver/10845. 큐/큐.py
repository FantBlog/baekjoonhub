import sys
n = int(sys.stdin.readline())
que = []
for _ in range(n):
    order = sys.stdin.readline()
    if order[:2] == 'pu':
        od,x = order.split()
        que.append(x)
    elif order[:2] == 'po':
        if len(que):
            print(que.pop(0))
        else:
            print('-1')
    elif order[:2] == 'si':
        print(len(que))
    elif order[:2] == 'em':
        if len(que):
            print('0')
        else:
            print('1')
    elif order[:2] == 'fr':
        if len(que):
            print(que[0])
        else:
            print('-1')
    else:
        if len(que):
            print(que[-1])
        else:
            print('-1')