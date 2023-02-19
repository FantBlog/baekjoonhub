def cleen(r,c,d):
    count = 0
    while True:
        
        if room[r][c] == 0: # 1. 청소 안되면 청소
            room[r][c] = 2
            count += 1
            
        for dr, dc in dd:
            if room[r + dr][c + dc] == 0: # 청소안된곳 있으면
                d -= 1 # 시계 반대 90도

                if d < 0:
                    d += 4

                if d > 3:
                    d -= 4
                
                if room[r + dd[d][0]][c + dd[d][1]] == 0: # 회전후 보는곳
                    # 범위 안이고 청소 안되어있으면
                    r += dd[d][0]
                    c += dd[d][1]
                break
        
        else: # 청소가 다 되있으면
            if room[r - dd[d][0]][c - dd[d][1]] == 1: # 벽이면
                return count
            else: # 아니면 후진
                r -= dd[d][0]
                c -= dd[d][1]
            continue

dd = [ # 북동남서
    # dr, dc
    (-1,0),
    (0,1),
    (1,0),
    (0,-1)
]
    
R, C = map(int,input().split())
r1, c1, d = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(R) ]
print(cleen(r1,c1,d))