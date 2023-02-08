import sys
t = int(sys.stdin.readline())
j = int()
for _ in range(t):
    a = sys.stdin.readline()
    if 'add' in a:
        _, b = a.split()
        b = int(b) - 1
        j = j | (1<<b)
    elif 'remove' in a:
        _, b = a.split()
        b = int(b) - 1
        j = j & ~(1<<b)
    elif 'check' in a:
        _, b = a.split()
        b = int(b) - 1
        if j & (1<<b):
            print(1)
        else:
            print(0)
    elif 'toggle' in a:
        _, b = a.split()
        b = int(b) - 1
        j = j ^ (1<<b)
    elif 'all' in a[:3]:
        j = ~(1<<20)
    elif 'empty' in a:
        j = j & 0