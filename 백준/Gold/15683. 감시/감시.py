# 15683번 감시
def cctv(x, y ,dirt): # 칠해주는 함수
    if dirt > 3:
        dirt -= 4
    elif dirt < 0:
        dirt += 4

    # if x == 4 and y == 4:
    #     print(x,y, dirt)

    nx = x + dx[dirt]
    ny = y + dy[dirt]

    if nx < 0 or ny < 0 or nx >= M or ny >=N: #범위 밖
        return 0
    
    if office[ny][nx] == 6: # 벽
        return 0
    
    elif office[ny][nx] == 0:
        office[ny][nx] = 9
        cctv(nx,ny,dirt)

    else:
        cctv(nx,ny,dirt)
    
def cctv5(x, y): # 5번은 일단 다 칠함
    for direction in range(4):
        cctv(x, y ,direction)

def allcctv(i):
    global mn

    if i == A:
        for a in cctv5_list:
            cctv5(a[0],a[1])
        for j in range(A):
            if arr[j][1] == 1:
                cctv(arr[j][2], arr[j][3] ,arr[j][0])
            
            elif arr[j][1] == 2:
                cctv(arr[j][2], arr[j][3] ,arr[j][0])
                cctv(arr[j][2], arr[j][3] ,arr[j][0] + 2)

            elif arr[j][1] == 3:
                cctv(arr[j][2], arr[j][3] ,arr[j][0])
                cctv(arr[j][2], arr[j][3] ,arr[j][0] + 1)

            elif arr[j][1] == 4:
                cctv(arr[j][2], arr[j][3] ,arr[j][0])
                cctv(arr[j][2], arr[j][3] ,arr[j][0] + 1)
                cctv(arr[j][2], arr[j][3] ,arr[j][0] + 2)

        # 사각지대 수 세기
        total = 0
        for y in range(N):
            total += office[y].count(0)

        if total < mn:
            # print(*office,sep='\n')
            mn = total
        
        # 다 세고 나면 초기화
        for y in range(N):
            for x in range(M):
                if office[y][x] == 9:
                    office[y][x] = 0
        return
    
    for j in range(4):
        arr[i][0] = j
        allcctv(i+1)



N, M = map(int,input().split())
office = [list(map(int,input().split())) for _ in range(N)]

mn = M*N
dx = [1,0,-1,0]
dy = [0,1,0,-1]


cctv5_list = []
for x in range(M):
    for y in range(N):
        if office[y][x] == 5:
            cctv5_list.append((x,y))


arr = []
for x in range(M):
    for y in range(N):
        if office[y][x] == 1:
            arr.append([0,1,x,y])
        elif office[y][x] == 2:
            arr.append([0,2,x,y])
        elif office[y][x] == 3:
            arr.append([0,3,x,y])
        elif office[y][x] == 4:
            arr.append([0,4,x,y])

A = len(arr)

allcctv(0)
print(mn)