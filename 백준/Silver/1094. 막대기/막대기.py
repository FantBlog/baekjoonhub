num = 6
stick = 1<<num
x = int(input())

count = 0
for j in range(num+1):
    if x & (1<<j):
        count += 1
print(count)