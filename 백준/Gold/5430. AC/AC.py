import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for test_case in range(1,T+1):
    order = input().rstrip('\n').replace('RR', '')
    n = int(input())
    numbers = deque(map(int,input().lstrip('[').rstrip(']\n').replace(',',' ').split()))
    
    error = True

    if n < order.count('D'):
        print('error')
        continue

    reverse = True
    for od in order:
        if od == 'R':
            if reverse:
                reverse = False
            else:
                reverse = True
        elif od == 'D':
            try:
                if reverse:
                    numbers.popleft()
                else:
                    numbers.pop()
            except:
                error = False
                print('error')
                break
    if error:
        print('[',end='')
        if reverse:
            print(*numbers,sep=',',end='')
        else:
            numbers.reverse()
            print(*numbers,sep=',',end='')
        print(']')