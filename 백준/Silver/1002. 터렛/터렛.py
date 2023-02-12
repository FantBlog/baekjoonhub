import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
        continue
        
    d = abs(((x2-x1)**2 + (y2-y1)**2)** 0.5)
    sumr = r1 + r2
    subr = abs(r1 - r2)
    if sumr > d > subr:
        print(2)
    elif sumr == d or subr == d:
        print(1)
    else:
        print(0)