from collections import deque

def turn(i, dirt):
    if dirt == 1:
        tob[i].appendleft(tob[i].pop())
    else:
        tob[i].append(tob[i].popleft())

tobs = int(input())
tob = [deque(map(int,list(input()))) for _ in range(tobs)]

N = int(input())
for _ in range(N):
    num, dirt = map(int,input().split()) # 돌릴 톱니, 방향
    num -= 1

    result = [(num,dirt)] # 얘는 돌림
    
    start = num
    re_dirt = dirt * -1
    while True:
        if start + 1 >= tobs: # 다음 톱니가 넘치면
            break
        
        if tob[start][2] != tob[start + 1][6]:
            result.append((start + 1, re_dirt))
            re_dirt *= -1
            start += 1
        else:
            break

    start = num
    re_dirt = dirt * -1
    while True:
        if start - 1 < 0: # 다음 톱니가 넘치면
            break
        
        if tob[start][6] != tob[start - 1][2]:
            result.append((start - 1, re_dirt))
            re_dirt *= -1
            start -= 1
        else:
            break
    
    for tb, drt in result:
        turn(tb, drt)
        
total = 0
for que in tob:
    if que[0] == 1:
        total += 1
print(total)