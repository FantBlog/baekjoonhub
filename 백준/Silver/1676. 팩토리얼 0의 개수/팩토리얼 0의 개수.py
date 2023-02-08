num = int(input())
if num == 0:
    print('0')
    exit()
result = 0
temp = num
while temp >= 5:
    result += temp //5
    temp //= 5
print(result)