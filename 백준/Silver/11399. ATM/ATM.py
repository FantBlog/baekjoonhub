import sys
n = int(sys.stdin.readline())
time = sorted(list(map(int,sys.stdin.readline().split())))
total = 0
for i in range(n):
    total += (n-i)*time[i]
print(total)