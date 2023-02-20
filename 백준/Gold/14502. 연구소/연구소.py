def clean(): # 연구소 청소
    for r in range(R):
        for c in range(C):
            if lab[r][c] == 3:
                lab[r][c] = 0

def cnt(): # 안전구역 세주기
    total = 0
    for r in range(R):
        total += lab[r].count(0)
    return total

def safe(): # 감염시키기
    stack = []
    for vls in vilus:
        stack.append(vls)

        while stack:
            r,c = stack.pop()
            for i in range(4):

                if not 0 <= r + dd[i][0] < R: # 범위 안 체크
                    continue
                if not 0 <= c + dd[i][1] < C:
                    continue

                if lab[r + dd[i][0]][c + dd[i][1]] == 0: # 빈칸이면
                    lab[r + dd[i][0]][c + dd[i][1]] = 3 # 감염
                    stack.append((r + dd[i][0], c + dd[i][1]))

    total = cnt()
    clean()
    return total

def check(): # 벽 3개 위치 체크
    count = 0
    for i in walls:
        r, c = divmod(i,C)
        if lab[r][c] == 0:
            count += 1
    
    if count != 3: # 벽 3개 못두면
        return 0

    for i in walls: # 벽 세움
        r, c = divmod(i,C)
        lab[r][c] = 1
    
    # print(walls)
    total = safe()

    for i in walls: # 벽 돌려놈
        r, c = divmod(i,C)
        lab[r][c] = 0
    
    return total

def protect(deep): # 벽 3개 경우의수 재귀
    global mx
    if deep == 3:
        total = check()
        if total > mx:
            mx = total
        return
        
    for i in range(Size):
        if i not in walls:
            walls.append(i)
            protect(deep+1)
            walls.pop()

dd = [
    (0,1),
    (0,-1),
    (1,0),
    (-1,0)
]
R, C = map(int,input().split())
Size = R*C
lab = [list(map(int,input().split())) for _ in range(R)]

mx = 0
walls = []

vilus = []
for r in range(R):
    for c in range(C):
        if lab[r][c] == 2:
            vilus.append((r,c))

protect(0)
print(mx)