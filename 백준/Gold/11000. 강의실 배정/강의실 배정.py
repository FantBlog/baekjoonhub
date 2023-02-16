import sys
import heapq

input = sys.stdin.readline
n = int(input())
timetable = []
count = 0
for i in range(n):
    timetable.append(tuple(map(int,input().split())))
timetable.sort(key=lambda x:(x[0],x[1]))
time = []
heapq.heappush(time,timetable[0][1])

for i in range(1,n):
    if timetable[i][0] >= time[0]:
        heapq.heappop(time)
        heapq.heappush(time,timetable[i][1])
    else:
        heapq.heappush(time,timetable[i][1])


print(len(time))