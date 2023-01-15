import sys
T = int(input())
for i in range(1,1+T):
    a,b = map(int,sys.stdin.readline().split())
    print(f'Case #{i}: {a+b}')