import sys
input = sys.stdin.readline
k, n = map(int,input().split())
line = []
for _ in range(k):
    line.append(int(input()))
start = 0
end = max(line)

while True:
    center = (start+end)//2
    if start + 1 >= end:
        total = 0
        for lin in line:
            total += lin // end
        if total < n:
            print(start)
            break
        else:
            print(end)
            break

    total = 0
    for lin in line:
        total += (lin // center)
    if n > total:
        end = center
    else:
        start = center