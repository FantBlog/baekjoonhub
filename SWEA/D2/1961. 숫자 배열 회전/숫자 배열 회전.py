T = int(input())
for test_case in range(1, T + 1):
    tr = int(input())

    line = []
    temp = []
    for i in range(tr):
        line.append(0)
    for i in range(tr):
        temp.append(line)

    for i in range(tr):
        temp[i] = list(map(int, input().split()))
    print(f'#{test_case}')
    rt=tr-1
    for i in range(tr):
        for j in range(tr):
            print(temp[rt-j][i], end='')
        print(' ', end='')
        for j in range(tr):
            print(temp[rt-i][rt-j], end='')
        print(' ', end='')
        for j in range(tr):
            print(temp[j][rt-i], end='')
        print()