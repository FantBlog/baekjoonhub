import sys
t = int(sys.stdin.readline())
a = sys.stdin.readlines()
b = []
for i in range(t):
    b.append(int(a[i].rstrip('\n')))
b = sorted(b)
for i in range(t):
    print(b[i])