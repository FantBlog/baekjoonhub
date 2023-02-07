from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    want = [False]*n
    want[m] = True
    lst = deque(zip(map(int,input().split()),want))
    count = 0
    while True:
        if lst[0][0] == max(lst)[0]:
            count += 1
            if lst.popleft()[1]:
                break
        else:
            lst.append(lst.popleft())
    print(count)