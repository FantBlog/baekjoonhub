def is_bingo(bingo):
    bnt = 0
    for i in range(5):
        if bingo[i] == [0, 0, 0, 0, 0]:
            bnt += 1
    for i in range(5):
        cnt_bingo = 0
        for j in range(5):
            if bingo[j][i] == 0:
                cnt_bingo += 1
        if cnt_bingo > 4:
            bnt += 1
    cnt_bingo = 0
    for i in range(5):
        if bingo[i][i] == 0:
            cnt_bingo += 1
    if cnt_bingo > 4:
        bnt += 1

    cnt_bingo = 0
    for i in range(5):
        if bingo[4 - i][i] == 0:
            cnt_bingo += 1
    if cnt_bingo > 4:
        bnt += 1

    if bnt > 2:
        return True
    else:
        return False

bingo = [[0] for _ in range(5)]
lotto = []
for i in range(5):
    bingo[i] = list(map(int, input().split()))
for _ in range(5):
    lotto += list(map(int, input().split()))

cnt = 0
end = False
for num in range(25):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == lotto[num]:
                cnt += 1
                bingo[i][j] = 0
            if is_bingo(bingo):
                end = True
                break
        if end:
            break
    if end:
        break
print(cnt)