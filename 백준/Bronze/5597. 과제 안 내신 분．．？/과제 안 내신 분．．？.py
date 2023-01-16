lst = []
for i in range(30):
    lst.append(0)

for i in range(28):
    lst[int(input())-1] += 1

idx = 0
for i in lst:
    if i == 0:
        print(idx+1)
    idx += 1