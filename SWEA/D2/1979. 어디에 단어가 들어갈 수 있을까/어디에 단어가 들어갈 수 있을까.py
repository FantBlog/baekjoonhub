T = int(input())
for test_case in range(1, T+1):
    data = input().split()
    a = int(data[0])
    b = int(data[1])
    matrix = []
    temp = []
    result = 0
    for i in range(a):
        temp.append(0)
    for i in range(a):
        matrix.append(temp)
    for i in range(a):
        matrix[i] = list(map(int, input().split()))
    for i in range(a):
        save = 0
        ans = []
        for j in range(a):
            if matrix[i][j] == 1:
                save += 1
            elif save == 0:
                ans.append(save)
            else:
                ans.append(save)
                save = 0
                ans.append(save)
            if j == a-1 and save != 0:
                ans.append(save)
        for q in ans:
            if q == b:
                result += 1
        save = 0
        ans = []
        for j in range(a):
            if matrix[j][i] == 1:
                save += 1
            elif save == 0:
                ans.append(save)
            else:
                ans.append(save)
                save = 0
                ans.append(save)
            if j == a - 1 and save != 0:
                ans.append(save)
        for q in ans:
            if q == b:
                result += 1
    print(f'#{test_case} {result}')