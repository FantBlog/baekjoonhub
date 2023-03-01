import sys
import heapq
def input(): return sys.stdin.readline().rstrip()

for _ in range(int(input())):
    N = int(input())
    max_hip = []
    min_hip = []
    vis = set()
    leng = 0
    cnt = 0
    for _ in range(N):
        O, num = input().split()
        num = int(num)

        if O == 'I':
            heapq.heappush(max_hip,(-num,cnt))
            heapq.heappush(min_hip,(num,cnt))
            leng += 1
            cnt += 1

        elif num > 0 and max_hip:
            while True:
                if not max_hip:
                    break
                _,a = heapq.heappop(max_hip)
                if a not in vis:
                    vis.add(a)
                    leng -= 1
                    break

        elif min_hip:
            while True:
                if not min_hip:
                    break
                _,a = heapq.heappop(min_hip)
                if a not in vis:
                    vis.add(a)
                    leng -= 1
                    break
        
    if leng > 0:
        while True:
            result_max, a = heapq.heappop(max_hip)
            if a not in vis:
                break
        while True:
            result_min, a = heapq.heappop(min_hip)
            if a not in vis:
                break
        print(-result_max,result_min)
    else:
        print('EMPTY')