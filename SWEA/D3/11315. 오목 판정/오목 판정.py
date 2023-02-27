for tc in range(1,int(input())+1):
    N = int(input())
    board = [list(map(lambda x: (1 if x == 'o' else 0) , input())) for _ in range(N)]
    
    result = 'NO'
    for r in range(N):
        for c in range(N-4):
            if sum(board[r][c:c+5]) == 5:
                result = 'YES'
    
    for c in range(N):
        for r in range(N-4):
            if sum(board[r+i][c] for i in range(5)) == 5:
                result = 'YES'
    
    for r in range(N-4):
        for c in range(N-4):
            if sum(board[r+i][c+i] for i in range(5)) == 5:
                result = 'YES'

    for r in range(4,N):
        for c in range(N-4):
            if sum(board[r-i][c+i] for i in range(5)) == 5:
                result = 'YES'
    
    print(f'#{tc} {result}')