nan_list = list()
for _ in range(9):
    nan_list.append(int(input()))
nan_list = sorted(nan_list)
brk = False
for i in range(8):
    for j in range(i+1,9):
        result = 0
        for o in range(9):
            if not(o == i or o == j):
                result += nan_list[o]
        if result == 100:
            brk = True
            for o in range(9):
                if not(o == i or o == j):
                    print(nan_list[o])
            break
    if brk:
        break