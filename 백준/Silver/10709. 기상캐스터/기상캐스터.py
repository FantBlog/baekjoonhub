R, C = map(int,input().split())
sky = [list(input()) for _ in range(R)]
for r in range(R):
    cloud = False
    for c in range(C):
        if sky[r][c] == 'c':
            cnt = 0
            sky[r][c] = cnt
            cloud = True
        elif cloud:
            cnt += 1
            sky[r][c] = cnt
        else:
            sky[r][c] = -1
for r in range(R):
    print(*sky[r])