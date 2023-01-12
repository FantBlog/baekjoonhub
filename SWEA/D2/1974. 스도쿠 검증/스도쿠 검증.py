T = int(input())

sdoku = []
for i in range(9):
    sdoku.append([0,0,0,0,0,0,0,0,0])

for test_case in range(1, T+1):
    answer = 1
    for i in range(9):
        sdoku[i] = input().split()

    for i in range(9):
        for j in range(9):

            for o in range(9):
                if i != o and sdoku[i][j] == sdoku[o][j]:
                    answer -= 1
            for o in range(9):
                if j != o and sdoku[i][j] == sdoku[i][o]:
                    answer -= 1
            for o in range(3):
                for p in range(3):
                    x = ((i // 3) * 3 )+ ((i + o) % 3)
                    y = ((j // 3) * 3 )+ ((j + p) % 3)
                    if i != x and j != y and sdoku[i][j] == sdoku[x][y]:
                        answer -= 1
    if answer < 1:
        answer = 0
    print(f'#{test_case} {answer}')