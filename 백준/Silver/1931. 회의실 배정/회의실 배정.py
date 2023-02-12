import sys
input = sys.stdin.readline
n = int(input())
timetable = []
count = 0
for i in range(n):
    timetable.append(tuple(map(int,input().split())))
timetable.sort(key=lambda x:(x[1],x[0]))
time = (0,0)
for i in range(n):
    if time[1] <= timetable[i][0]:
        time = timetable[i]
        count += 1
print(count)