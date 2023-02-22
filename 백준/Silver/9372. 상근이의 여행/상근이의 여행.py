import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a,b=map(int,input().split())
    for _ in range(b):
        input()
    print(a-1)