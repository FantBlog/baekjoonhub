import sys
input = sys.stdin.readline

def colorpaper(c_paper,size):
    center = size // 2
    full = int(size ** 2)
    white = 0
    blue = 0
    count = 0
    for x in range(size):
        for y in range(size):
            count += c_paper[y][x]
    if count == full:
        white += 0
        blue += 1
        return white, blue
    elif count == 0:
        white += 1
        blue += 0
        return white, blue
    else:
        a,b = colorpaper([c_paper[i][:center] for i in range(center)],center)
        white += a
        blue += b
        a,b = colorpaper([c_paper[i][center:] for i in range(center)],center)
        white += a
        blue += b
        a,b = colorpaper([c_paper[i][:center] for i in range(center,size)],center)
        white += a
        blue += b
        a,b = colorpaper([c_paper[i][center:] for i in range(center,size)],center)
        white += a
        blue += b
    return white, blue

n = int(input())
paper = [list(map(int,input().split())) for _ in range(n)]
print(*colorpaper(paper,n),sep='\n')