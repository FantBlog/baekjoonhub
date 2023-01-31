import sys
N, K = map(int,sys.stdin.readline().rstrip('\n').split())
room_list = list()
for i in range(6):
    room_list.append([0,0])

for i in range(N):
    gender, grade = map(int,sys.stdin.readline().rstrip('\n').split())
    room_list[grade-1][gender] += 1

count = 0
for i in range(6):
    for j in range(2):
        count += room_list[i][j] // K
        count += room_list[i][j] % K
print(count)