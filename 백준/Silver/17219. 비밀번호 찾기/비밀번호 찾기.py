import sys
n, m = map(int,sys.stdin.readline().split())
pss_list = {}
for _ in range(n):
    a,b = sys.stdin.readline().split()
    pss_list[a] = b
for _ in range(m):
    print(pss_list[input()])