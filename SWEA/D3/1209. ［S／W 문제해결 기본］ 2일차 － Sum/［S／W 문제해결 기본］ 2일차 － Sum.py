for a in range(1,11):
    test_case = int(input())

    data = []
    for i in range(100):
        data.append(list(map(int,input().split())))

    max = 0
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += data[i][j]

        if max < temp:
            max = temp

    for i in range(100):
        temp = 0
        for j in range(100):
            temp += data[j][i]

        if max < temp:
            max = temp

    for i in range(100):
        temp = 0
        temp += data[i][i]

        if max < temp:
            max = temp

    print(f'#{a} {max}')