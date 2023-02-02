x, y = map(int,input().split())
t = int(input())
x_cut = []
y_cut = []
x_len = [x]
y_len = [y]
for _ in range(t):
    h , l = map(int,input().split())
    if h:
        x_cut.append(l)
    else:
        y_cut.append(l)
x_cut.sort()
y_cut.sort()
if len(x_cut) > 0:
    x_len = []
    x_len.append(x_cut[0])
    if len(x_cut) >= 2:
        for i in range(len(x_cut)-1):
            x_len.append(x_cut[i+1] - x_cut[i])
    x_len.append(x-x_cut[-1])
if len(y_cut) > 0:
    y_len = []
    y_len.append(y_cut[0])
    if len(y_cut) >= 2:
        for i in range(len(y_cut)-1):
            y_len.append(y_cut[i+1] - y_cut[i])
    y_len.append(y-y_cut[-1])
print(max(x_len)*max(y_len))