import math
tc = int(input())
for _ in range(tc):
    a, b = map(int,input().split())
    n = abs(a-b)
    ban = math.floor(math.sqrt(n))
    if n < 4:
        print(n)
    elif int(ban) == math.sqrt(n):
        print(2 * ban - 1)
    elif n <= ban**2 + ban:
        print(2 * ban)
    else:
        print(2 * ban + 1)