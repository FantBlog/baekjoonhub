n = input()
count=[0]*10
for i in n:
    count[int(i)] += 1
for i in range(9,-1,-1):
    print(str(i)*count[i],end='')