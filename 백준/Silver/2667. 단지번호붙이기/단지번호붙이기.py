N = int(input())
home_map = []
for i in range(N):
    home_map.append(list(map(int,input())))
def check(y,x):
    result = 0
    if home_map[y][x] == 1:
        home_map[y][x] = 2
        result += 1
    if y > 0 and home_map[y-1][x] == 1:
        home_map[y-1][x] += 1
        result += check(y-1,x) + 1
    if N-1 > y and home_map[y+1][x] == 1:
        home_map[y+1][x] += 1
        result += check(y+1,x) + 1
    if x > 0 and home_map[y][x-1] == 1:
        home_map[y][x-1] += 1
        result += check(y,x-1) + 1
    if N-1 > x and home_map[y][x+1] == 1:
        home_map[y][x+1] += 1
        result += check(y,x+1) + 1
    return result
count = list()
for y in range(N):
    for x in range(N):
        if home_map[y][x] == 1:
            size = check(y,x)
            count.append(size)
count.sort()
print(len(count))
for i in count:
    print(i)