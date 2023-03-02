import copy
dd = (
    (-1,0),
    (-1,-1),
    (0,-1),
    (1,-1),
    (1,0),
    (1,1),
    (0,1),
    (-1,1),
)
def movefish(arr,data):
    for i in range(1,17):
        # print(*arr,sep='\n',end='\n\n')
        r, c = data[i][0] # r,c = (r,c)
        for _ in range(8): # 한바퀴 돌면 종료
            d = data[i][1]
            if d == -1: # 죽은 물고기라면
                break
            
            if 0 <= r+dd[d][0] <size and 0 <= c+dd[d][1] < size: # 범위 안이고
                if arr[r+dd[d][0]][c+dd[d][1]] == 0: # 바라보는 칸이 빈칸이라면
                    # 서로의 물고기 위치 정보 교환
                    data[i][0] = (r+dd[d][0],c+dd[d][1])
                    arr[r][c], arr[r+dd[d][0]][c+dd[d][1]] = arr[r+dd[d][0]][c+dd[d][1]], arr[r][c]
                    break
                if arr[r+dd[d][0]][c+dd[d][1]] > 0: # 바라보는 칸이 물고기라면
                    # 서로의 물고기 위치 정보 교환
                    data[i][0], data[arr[r+dd[d][0]][c+dd[d][1]]][0] = data[arr[r+dd[d][0]][c+dd[d][1]]][0], data[i][0]
                    arr[r][c], arr[r+dd[d][0]][c+dd[d][1]] = arr[r+dd[d][0]][c+dd[d][1]], arr[r][c]
                    break
                
            # 이동못해서 45도 회전
            data[i][1] += 1
            if data[i][1] > 7:
                data[i][1] = 0
        
    return arr, data
            
                
def shark(r, c, total, seas, fishs, deeps):
    global mx
    
    new_sea = copy.deepcopy(seas)
    new_fish = copy.deepcopy(fishs)

    total += new_sea[r][c] # 먹은 총양 에 추가
    new_fish[0] = new_fish[new_sea[r][c]] # 상어의 위치, 방향 저장
    
    if mx < total:
        mx = total
    
    new_fish[new_sea[r][c]] = [(-1,-1),-1] # 해당 물고기 사망 # 방향 -1
    new_sea[r][c] = -1 # 상어로 설정
    
    new_sea, new_fish = movefish(new_sea,new_fish)
    
    s_r, s_c = new_fish[0][0]
    d = new_fish[0][1]
    
    for i in range(1,size+1):
        if not(0 <= s_r + dd[d][0]*i < size and 0 <= s_c + dd[d][1]*i < size): # 범위 밖이면 그만
            return
        
        if new_sea[s_r + dd[d][0]*i][s_c + dd[d][1]*i] > 0: # 물고기라면
            new_sea[r][c] = 0 # 이동했으니 빈칸으로
            shark(s_r + dd[d][0]*i, s_c + dd[d][1]*i, total, new_sea, new_fish, deeps + 1)

size = 4
sea = []

fish = [0] * (size * size + 1)
for r in range(size):
    nums = list(map(int,input().split()))
    sea.append([nums[i] for i in range(0,8,2)])
    for c in range(4):
        fish[nums[c*2]] = [(r,c),nums[c*2+1]-1]

mx = 0

shark(0,0,0,sea,fish,0)

print(mx)