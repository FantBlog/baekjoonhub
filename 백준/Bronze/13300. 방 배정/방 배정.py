import sys
input = sys.stdin.readline
n,k = map(int,input().split())
room_list = list()
for _ in range(6):
    room_list.append([0,0])
for _ in range(n):
    gender, grade = map(int,input().split())
    room_list[grade-1][gender] += 1
count = 0
for i in range(6):
    for j in range(2):
        count += room_list[i][j] // k + room_list[i][j] % k
print(count)