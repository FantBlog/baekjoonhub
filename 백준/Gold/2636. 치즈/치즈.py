import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

dd = [
    (0,1),
    (0,-1),
    (1,0),
    (-1,0)
]
def air(r,c):
    for dr, dc in dd:
        if not 0 <= r + dr < R or not 0 <= c + dc < C:
            continue # 범위 밖
        if not air_arr[r + dr][c + dc] and cheese[r + dr][c + dc] == 0:
            air_arr[r + dr][c + dc] = True
            airque.append((r + dr,c + dc))

def chz(r,c):
    count = 0
    for dr, dc in dd:
        if not 0 <= r + dr < R or not 0 <= c + dc < C:
            continue # 범위 밖
        if air_arr[r + dr][c + dc]:
            count += 1

    if count >= 1:
        return True
    else:
        return False

R, C = map(int,input().split())
cheese = [list(map(int,input().split())) for _ in range(R)]
time = 0

while True:
    time += 1
    
    air_arr = [[False]*C for _ in range(R)]

    airque = deque()

    for r in range(R):
        for c in [0,C-1]:
            if air_arr[r][c] == False and not cheese[r][c]: # 치즈가아니고, 외부공기가 아닐때
                airque.append((r,c)) # 큐에추가
                air_arr[r][c] = True # 지나온곳
                while airque:
                    air(*airque.popleft())

    for c in range(C):
        for r in [0,R-1]:
            if air_arr[r][c] == False and not cheese[r][c]: # 치즈가아니고, 외부공기가 아닐때
                airque.append((r,c)) # 큐에추가
                air_arr[r][c] = True # 지나온곳
                while airque:
                    air(*airque.popleft())

    total = 0
    result = 0
    for num in range(R*C):
        r,c = divmod(num,C)

        if cheese[r][c] == 1:
            if chz(r,c):
                result += 1
                cheese[r][c] = 0 # 녹임
        if cheese[r][c] == 0:
            total += 1
    
    if total == R*C:
        print(time)
        print(result)
        break