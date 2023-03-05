def rotation(r,c,i):

    c += 1
    while c < C - i:
        arr[r][c], arr[r][c-1] = arr[r][c-1], arr[r][c]
        c += 1

    c -= 1

    r += 1
    while r < R - i:
        arr[r][c], arr[r-1][c] = arr[r-1][c], arr[r][c]
        r += 1

    r -= 1

    c -= 1
    while c >= i:
        arr[r][c], arr[r][c+1] = arr[r][c+1], arr[r][c]
        c -= 1

    c += 1

    r -= 1
    while r > i:
        arr[r][c], arr[r+1][c] = arr[r+1][c], arr[r][c]
        r -= 1

    r += 1

    
R, C, Rot = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(R)]

for _ in range(Rot):
    for i in range(min(R,C)//2):
        rotation(i,i,i)

for r in range(R):
    print(*arr[r])