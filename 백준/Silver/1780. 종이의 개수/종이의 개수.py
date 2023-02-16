def color(num):
    global jong1
    global jong2
    global jong3

    if num == -1:
        jong1 += 1
    elif num == 1:
        jong3 += 1
    else:
        jong2 += 1

def paper(x_s,y_s,n):
    if n == 1:
        color(arr[y_s][x_s])
        return 
    
    C = n // 3
    check = arr[y_s][x_s]
    
    for x in range(x_s,x_s+n):
        for y in range(y_s,y_s+n):

            if arr[y][x] != check: # 시작점이랑 다르면 다 같은거아님
                paper(x_s, y_s,C)
                paper(x_s, y_s + C,C)
                paper(x_s, y_s + 2 * C,C)

                paper(x_s + C, y_s, C)
                paper(x_s + C, y_s + C,C)
                paper(x_s + C, y_s + 2 * C,C)
                
                paper(x_s + 2 * C, y_s, C)
                paper(x_s + 2 * C, y_s + C,C)
                paper(x_s + 2 * C, y_s + 2 * C,C)
                return # 재귀호출하고 종료
    
    color(check)

        



n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
jong1 = 0
jong2 = 0
jong3 = 0
paper(0,0,n)
print(jong1, jong2, jong3)