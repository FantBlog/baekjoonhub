def findQueens(n):
    arr = []
    answer = 0

    for _ in range(n):
        arr.append(0)

    def f(deep, arr, n):
        nonlocal answer
        if (deep > n):
            answer += 1
            return
        

        for index in range(n):
            if (arr[index] > 0): continue
            
            x = False
            for i in range(n):
                if (arr[i] == 0): continue
                if (abs(deep - arr[i]) == abs(index - i)):
                    x = True
                    break

            if x: continue
            
            arr[index] = deep
            f(deep + 1, arr, n)
            arr[index] = 0

    f(1, arr, n)

    return answer

print(findQueens(int(input())))