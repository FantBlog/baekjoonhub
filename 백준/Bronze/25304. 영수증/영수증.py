T = int(input())
s = int(input())
c = 0
for i in range(s):
    a, b = map(int, input().split())
    c += a * b
if T == c:
    print('Yes')
else:
    print('No')