all = int(input())
num = list(map(int, input().split()))
check = 0
check_reverse = 0
big = 0
for n in range(all-1):
    if num[n+1] >= num[n]:
        check += 1
    else:
        check = 0
    if num[n+1] <= num[n]:
        check_reverse += 1
    else:
        check_reverse = 0
    if max(check, check_reverse) > big:
        big = max(check, check_reverse)
    
print(big+1)