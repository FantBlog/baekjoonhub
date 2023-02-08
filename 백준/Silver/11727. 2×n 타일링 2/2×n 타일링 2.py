fire = [1,3,5]
n = int(input())
if n < 3:
    print(fire[n-1])
    exit()
for i in range(3,n):
    if i % 2:
        fire.append(fire[i-1]*2 + 1)
    else:
        fire.append(fire[i-1]*2 - 1)
print(fire[n-1]%10007)