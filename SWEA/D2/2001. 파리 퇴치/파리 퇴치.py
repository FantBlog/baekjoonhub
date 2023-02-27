for tc in range(1,int(input())+1):
    N, M = map(int,input().split())
    pari = [list(map(int,input().split())) for _ in range(N)]
    
    mx = 0
    for r in range(1+N-M):
        for c in range(1+N-M):
            total = 0
            for i in range(M):
                for j in range(M):
                    total += pari[r+i][c+j]
            if total > mx:
                mx = total
    
    print(f'#{tc} {mx}')