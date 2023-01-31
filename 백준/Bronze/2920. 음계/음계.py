t = list(map(int,input().split()))
asc = True
des = True
for i in range(8):
    if t[i] != i+1:
        asc = False
    if t[i] != 8-i:
        des = False
if asc:
    print('ascending')
elif des:
    print('descending')
else:
    print('mixed')