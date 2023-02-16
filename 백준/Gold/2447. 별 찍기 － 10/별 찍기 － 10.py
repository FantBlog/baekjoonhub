def star(x_s,y_s,n):
    if n == 3:
        for x in range(x_s,x_s+n):
            for y in range(y_s,y_s+n):
                if not (x == x_s + 1 and y == y_s + 1):
                    result[y][x] = '*'
        return
    
    C = n//3
    star(x_s, y_s,C)
    star(x_s, y_s + C,C)
    star(x_s, y_s + 2 * C,C)

    star(x_s + C, y_s, C)

    star(x_s + C, y_s + 2 * C,C)
    
    star(x_s + 2 * C, y_s, C)
    star(x_s + 2 * C, y_s + C,C)
    star(x_s + 2 * C, y_s + 2 * C,C)

n = int(input())
result = [[' ']*n for _ in range(n)]
star(0,0,n)
for i in range(n):
    print(*result[i],sep='')