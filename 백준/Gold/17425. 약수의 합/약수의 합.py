import sys
input = sys.stdin.readline

bak = 1000000
lst = [1]*bak
for i in range(2,bak+1):
    for j in range(i,bak+1,i):
        lst[j-1] += i
for i in range(1,bak):
    lst[i] += lst[i-1]

t = int(input())
for _ in range(t):
    n = int(input())
    print(lst[n-1])