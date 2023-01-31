import sys
N = int(sys.stdin.readline().rstrip('\n'))
stack = list()
for n in range(N):
    order = sys.stdin.readline().rstrip('\n')
    if order[:3] == 'pus':
        stack.append(int(order.split()[1]))
        continue
    elif order[:3] == 'top':
        try:
            print(stack[-1])
            continue
        except:
            print('-1')
            continue
    elif order[:3] == 'siz':
        print(len(stack))
        continue
    elif order[:3] == 'emp':
        if len(stack):
            print('0')
            continue
        else:
            print('1')
            continue
    elif order[:3] == 'pop':
        try:
            print(stack.pop())
            continue
        except:
            print('-1')
            continue