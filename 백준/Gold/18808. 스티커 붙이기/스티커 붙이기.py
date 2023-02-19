import sys
def input(): return sys.stdin.readline().rstrip()

def push(stack):
    while stack:
        y, x = stack.pop()
        paper[y][x] = 1

def DFS(y, x, arr, paper): # 다음 이동한곳
    r = len(arr)
    c = len(arr[0]) 
    
    result = []
    
    for dx in range(x,x+c):
        for dy in range(y,y+r):
            if dx < 0 or dy < 0 or dx >= C or dy >= R: # 범위 밖이면
                continue
            if arr[dy-y][dx-x] == 1 and paper[dy][dx] == 0:
                result.append((dy,dx))

    return result

def chap_cal(arr, paper, su):
    for y in range(R - r + 1):
        for x in range(C - c + 1):

            result = DFS(y, x, arr, paper)

            if len(result) == su:
                push(result)
                return True

def chap_raw(arr, paper, su):
    for y in range(R - c + 1):
        for x in range(C - r + 1):

            result = DFS(y, x, arr, paper)

            if len(result) == su:
                push(result)
                return True

R, C, N = map(int,input().split()) # 전체 크기 , 붙이는 개수

paper = [[0]*C for _ in range(R)]

for _ in range(N):
    r, c = map(int,input().split()) # 붙일 크기

    monun = [list(map(int,input().split())) for _ in range(r)]
    monun_90 = [[0]*r for _ in range(c)]
    monun_180 = [[0]*c for _ in range(r)]
    monun_270 = [[0]*r for _ in range(c)]


    su = 0 # 칠할 전체 칸 수
    for y in range(r):
        su += monun[y].count(1)
        for x in range(c):
            if monun[y][x] == 1:
                monun_90[x][r-y-1] = 1
                monun_180[r-y-1][c-x-1] = 1
                monun_270[c-x-1][y] = 1
    
    if chap_cal(monun, paper, su):
        continue
    
    if chap_raw(monun_90, paper, su):
        continue
        
    if chap_cal(monun_180, paper, su):
        continue

    if chap_raw(monun_270, paper, su):
        continue
        
total = 0
for y in range(R):
    total += paper[y].count(1)
print(total)