for tc in range(1,int(input())+1):
    N = int(input())
    farm = [list(map(int,input())) for _ in range(N)]
    total = 0
    for r in range(N):
        for c in range(abs(r - N // 2) , N - abs(r - N // 2)):
            total += farm[r][c]
    print(f'#{tc} {total}')