result = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(4):
    l_x,l_y,r_x,r_y = map(int,input().split())
    for i in range(r_x - l_x):
        for j in range(r_y - l_y):
            result[l_x + i][l_y + j] = 1
count = 0
for i in range(100):
    for j in range(100):
        if result[i][j]:
            count += 1
print(count)
    
