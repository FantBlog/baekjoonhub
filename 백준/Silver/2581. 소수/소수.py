import math
def primenumber(number):
    isprime = True
    if number == 1:
        return False
    for j in range(2,number**0.5.__ceil__()):
        if number % j == 0 and number != j:
            isprime = False
            break
    if isprime:
        return True
    
M = int(input())
N = int(input())
num_set = set()
for i in range(M,N+1):
    if primenumber(i):
        num_set.add(i)

if len(num_set) == 0:
    print('-1')
else:
    print(sum(num_set))
    print(min(num_set))