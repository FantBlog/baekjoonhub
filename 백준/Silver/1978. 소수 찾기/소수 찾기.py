import math
T = int(input())
num_list = list(map(int,input().split()))
count = 0
for i in range(T):
    isprime = True
    if num_list[i] == 1:
        continue
    for j in range(2,num_list[i]**0.5.__ceil__()):
        if num_list[i] % j == 0 and num_list[i] != j:
            isprime = False
            break
    if isprime:
        count += 1
    

print(count)