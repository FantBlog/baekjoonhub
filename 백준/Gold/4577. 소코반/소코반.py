def move(order):
    if order == 'U':
        UP()
    elif order == 'L':
        LEFT()
    elif order == 'R':
        RIGHT()
    elif order == 'D':
        DOWN()

def UP():
    global player
    global targets
    r, c = player
    if World[r - 1][c] == '.': # 다음칸이 빈칸이면
        player = [r - 1, c]
        
        if World[r][c] == 'W': # 플레이어 시작점이 도착점이면
            World[r][c] = '+'
        else: # 아니면
            World[r][c] = '.'
        
        World[r-1][c] = 'w'
        
    elif World[r-1][c] in ('b','B') and World[r-2][c] not in ('#','b','B'): 
        # 다음칸이 박스이고  # 움직일수 있고
        player = [r - 1, c]
        
        if World[r-1][c] == 'B': # 지금 미는게 이미 골이라면
            World[r-1][c] = 'W'
            targets -= 1
        else:
            World[r-1][c] = 'w'
            
        if World[r][c] == 'W': # 플레이어 시작점이 도착점이면
            World[r][c] = '+'
        else: # 아니면
            World[r][c] = '.'
        
        if World[r-2][c] == '+': # 박스위가 도착점이면
            World[r-2][c] = 'B'
            targets += 1
        else: # 아니면
            World[r-2][c] = 'b'

def DOWN():
    global player
    global targets
    r, c = player
    if World[r + 1][c] == '.': # 다음칸이 빈칸이면
        player = [r + 1, c]
        
        if World[r][c] == 'W': # 플레이어 시작점이 도착점이면
            World[r][c] = '+'
        else: # 아니면
            World[r][c] = '.'
        
        World[r+1][c] = 'w'
    
    elif World[r + 1][c] in ('b','B') and World[r + 2][c] not in ('#','b','B'): 
        # 다음칸이 박스이고  # 움직일수 있고
        player = [r + 1, c]
        
        if World[r + 1][c] == 'B': # 지금 미는게 이미 골이라면
            World[r + 1][c] = 'W'
            targets -= 1
        else:
            World[r + 1][c] = 'w'
            
            
        if World[r][c] == 'W': # 플레이어 시작점이 도착점이면
            World[r][c] = '+'
        else: # 아니면
            World[r][c] = '.'
        
        if World[r + 2][c] == '+': # 박스위가 도착점이면
            World[r + 2][c] = 'B'
            targets += 1
        else: # 아니면
            World[r + 2][c] = 'b'

def LEFT():
    global player
    global targets
    r, c = player
    if World[r][c - 1] == '.': # 다음칸이 빈칸이면
        player = [r, c - 1]
        
        if World[r][c] == 'W': # 플레이어 시작점이 도착점이면
            World[r][c] = '+'
        else: # 아니면
            World[r][c] = '.'
        
        World[r][c-1] = 'w'
    
    elif World[r][c - 1] in ('b','B') and World[r][c - 2] not in ('#','b','B'): 
        # 다음칸이 박스이고  # 움직일수 있고
        player = [r, c - 1]
        
        if World[r][c - 1] == 'B': # 지금 미는게 이미 골이라면
            World[r][c - 1] = 'W'
            targets -= 1
        else:
            World[r][c - 1] = 'w'
            
            
        if World[r][c] == 'W': # 플레이어 시작점이 도착점이면
            World[r][c] = '+'
        else: # 아니면
            World[r][c] = '.'
        
        if World[r][c - 2] == '+': # 박스위가 도착점이면
            World[r][c - 2] = 'B'
            targets += 1
        else: # 아니면
            World[r][c - 2] = 'b'
            
def RIGHT():
    global player
    global targets
    
    r, c = player
    if World[r][c + 1] == '.': # 다음칸이 빈칸이면
        player = [r, c + 1]
        
        if World[r][c] == 'W': # 플레이어 시작점이 도착점이면
            World[r][c] = '+'
        else: # 아니면
            World[r][c] = '.'
        
        World[r][c+1] = 'w'
    
    elif World[r][c + 1] in ('b','B') and World[r][c + 2] not in ('#','b','B'): 
        # 다음칸이 박스이고  # 움직일수 있고
        player = [r, c + 1]
        
        if World[r][c] == 'W': # 플레이어 시작점이 도착점이면
            World[r][c] = '+'
        else: # 아니면
            World[r][c] = '.'
        
        
        if World[r][c + 1] == 'B': # 지금 미는게 이미 골이라면
            World[r][c + 1] = 'W'
            targets -= 1
        else:
            World[r][c + 1] = 'w'
        
        if World[r][c + 2] == '+': # 박스위가 도착점이면
            World[r][c + 2] = 'B'
            targets += 1
        else: # 아니면
            World[r][c + 2] = 'b'



tc = 1
while True:
    R, C = map(int,input().split())
    if R == 0 and C == 0:
        break
    World = [list(input()) for _ in range(R)]
    Order = list(input())
    
    # + 가 하나라도 있으면 게임 안끝남
    # + 가 다 지워지면 키입력 남아도 게임 종료
    targets = 0
    player = []
    tgt = set()
    for r in range(R):
        for c in range(C):
            if World[r][c] == '+' or World[r][c] == 'W':
                targets -= 1
                tgt.add((r,c))
            if World[r][c] == 'B':
                tgt.add((r,c))
            
            if World[r][c] == 'w' or World[r][c] == 'W':
                player = [r,c]

    
    for order in Order:
        move(order)
        if targets == 0:
            print(f'Game {tc}: complete')
            for text in World:
                print(*text,sep='')
            break
    else:
        print(f'Game {tc}: incomplete')
        for text in World:
            print(*text,sep='')
    tc += 1