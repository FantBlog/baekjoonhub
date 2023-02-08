import sys
input = sys.stdin.readline
n, m = map(int,input().split())
dd = set()
bo = set()
for _ in range(n):
    dd.add(input().rstrip('\n'))
    
for _ in range(m):
    bo.add(input().rstrip('\n'))

result = sorted(dd & bo)
print(len(result))
for i in result:
    print(i)