import sys
N = int(sys.stdin.readline().rstrip('\n'))
stack = list()
for n in range(N):
    order = sys.stdin.readline().rstrip('\n')
    if order[:3] == 'pus':
        stack.append(int(order.split()[1]))
    elif order[:3] == 'top':
        try:
            print(stack[-1])
        except:
            print('-1')
    elif order[:3] == 'siz':
        print(len(stack))
    elif order[:3] == 'emp':
        if len(stack):
            print('0')
        else:
            print('1')
    elif order[:3] == 'pop':
        try:
            print(stack.pop())
        except:
            print('-1')