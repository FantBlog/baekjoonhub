def st_white(text):
    count = 0
    if text != ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']:
        for idx,word in enumerate(text):
            if idx % 2:
                if word != 'B':
                    count += 1
            else:
                if word != 'W':
                    count += 1
    return count
def st_black(text):
    count = 0
    if text != ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']:
        for idx,word in enumerate(text):
            if idx % 2:
                if word != 'W':
                    count += 1
            else:
                if word != 'B':
                    count += 1
    return count
def is_chess_w(x,y):
    total = 0
    for j in range(y,y+8):
        if j % 2:
            total += st_black(chess[j][x:x+8])
        else:
            total += st_white(chess[j][x:x+8])
    return total

def is_chess_b(x,y):
    total = 0
    for j in range(y,y+8):
        if j % 2:
            total += st_white(chess[j][x:x+8])
        else:
            total += st_black(chess[j][x:x+8])
    return total

n,m = map(int,input().split())
chess = []
for _ in range(n):
    chess.append(list(input()))

mn = 64
for y in range(n-7):
    for x in range(m-7):
        temp = is_chess_w(x,y)
        if mn > temp:
            mn = temp
        temp = is_chess_b(x,y)
        if mn > temp:
            mn = temp
print(mn)