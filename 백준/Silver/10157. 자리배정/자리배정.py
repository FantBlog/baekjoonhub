import sys
# 10157 자리배정
c, r = map(int,input().split())
num = int(sys.stdin.readline())
C = c
R = r

if num > C * R:
    print('0')
    exit()

c -= 1
total = 0
cycle = 1
cnt = 1 # 세로, 가로
cnt2 =  0 # 위 오 / 아 왼
while True:

    if cnt % 2:
        total += r
        r -= 1
        cnt += 1
    else:
        total += c
        c -= 1
        cnt -= 1

    cnt2 += 1 # 위오 / 아왼 검증
    cnt2 = cnt2 % 4

    if cnt2 == 0: # 4 번 돌때마다
        cycle += 1  # 사이클 1 증가

    if total >= num:
        q = cycle-1 # 몇번째 바퀴인지
        chai = total - num # 차이
        if cnt % 2:  # 가로줄일때
            if cnt2 in [1,2]:
                print(f'{C-q-chai} {R-q}')
            else:
                print(f'{cycle+chai} {cycle-1}')
        else:  # 세로줄일때
            if cnt2 in [1,2]:
                print(f'{cycle} {R-q-chai}')
            else:
                print(f'{C-q} {cycle + chai}')
        break