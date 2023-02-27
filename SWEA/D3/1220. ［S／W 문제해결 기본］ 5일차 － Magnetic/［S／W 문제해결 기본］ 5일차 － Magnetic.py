for tc in range(1,11):
    size = int(input())
    # 1 = N 극 아래로, 2 = S 극 위로
    table = [list(map(int,input().split())) for _ in range(size)]
    result = 0
    for c in range(size):
        stack = []
        for r in range(size):
            if table[r][c] == 1:
                stack.append(table[r][c])
            elif table[r][c] == 2 and stack and stack[-1] == 1: # s극이고, 스택이 있고, 마지막이 1이면
                stack.clear()
                result += 1
    print(f'#{tc} {result}')