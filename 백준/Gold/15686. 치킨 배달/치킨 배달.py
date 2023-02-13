n,m = map(int,input().split())
world = [list(map(int,input().split())) for _ in range(n)]

chiken = list()
home = set()
for y in range(n):
    for x in range(n):
        if world[y][x] == 2:
            chiken.append((x,y))
        elif world[y][x] == 1:
            home.add((x,y))
min_min_list = []
for i in range(1<<len(chiken)):
    cnt = 0
    check = []
    for j in range(len(chiken)):
        if i & (1<<j):
            check.append(j)
            cnt += 1
    if cnt == m:
        min_list = []
        for hm in home:
            mn = n**2
            for ch in check:
                total = abs(hm[0]-chiken[ch][0]) + abs(hm[1]-chiken[ch][1])
                if total < mn:
                    mn = total
            min_list.append(mn)
        min_min_list.append(sum(min_list))
print(min(min_min_list))