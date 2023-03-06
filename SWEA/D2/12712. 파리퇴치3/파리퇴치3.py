def plu(r,c):
    total = -pari[r][c]
    for i in range(max(r+1-M,0), min(r+M,N)):
        total += pari[i][c]
    for j in range(max(c+1-M,0), min(c+M,N)):
        total += pari[r][j]
    return total

def mul(r,c):
    dd = (
        (-1,-1),
        (-1,1),
        (1,-1),
        (1,1)
    )
    total = pari[r][c]
    for idx in range(4):
        cnt = 1
        while cnt < M:
            if not(0 <= r+dd[idx][0]*cnt < N and 0 <= c+dd[idx][1]*cnt < N):
                break
            total += pari[r+dd[idx][0]*cnt][c+dd[idx][1]*cnt]
            cnt += 1
    return total
        

for tc in range(1,int(input())+1):
    N, M = map(int,input().split())
    pari = [list(map(int,input().split())) for _ in range(N)]
    mx = -1
    for r in range(N):
        for c in range(N):
            temp = plu(r,c)
            if temp > mx:
               mx = temp
               
            temp = mul(r,c)
            if temp > mx:
                mx = temp
    print(f'#{tc} {mx}')