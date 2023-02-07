import sys
n, m = map(int,sys.stdin.readline().split())
height = sorted(list(map(int,sys.stdin.readline().split())))
start = 0
end = height[-1]
while True:
    center = (start+end)//2
    if start+1 == end or start > end:
        total = 0
        for hei in height:
            if hei > end:
                total += hei - end
        if total >= m:
            print(end)
        else:
            print(start)
        break
    
    total = 0
    for hei in height:
        if hei > center:
            total += hei - center
        if total > m:
            break
    if total == m:
        print(center)
        break
    elif total > m:
        start = center + 1
    else:
        end = center - 1