import sys
def ant(x,y,t):
    x += t
    y += t
    x %= 2 * w
    y %= 2 * h
    if x > w:
        x = 2 * w - x
    if y > h:
        y = 2 * h - y
    print(x,y)
    return x, y
w,h = map(int,sys.stdin.readline().split())
x,y = map(int,sys.stdin.readline().split())
t = int(sys.stdin.readline())
ant(x,y,t)