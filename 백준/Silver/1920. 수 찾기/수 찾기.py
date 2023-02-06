import sys

def find(n,start,end):
    if start + 1 == end:
        if n in a[start:end+1]:
            return True
        return False

    center = (start + end) // 2
    if a[center] == n:
        return True
    elif a[center] > n:
        return find(n,start,center)
    else:
        return find(n,center,end)
    
    
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))

a.sort()

for num in b:
    if find(num,0,n):
        print('1')
    else:
        print('0')