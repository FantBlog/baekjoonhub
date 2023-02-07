def is_prime(num):
    for x in range(2,int(num**(1/2))+1):
        if num % x == 0:
            return False
    else:
        return True

def singi(num):
    if num > 10**(n-1):
        return True
    for i in range(10):
        temp = num*10+i
        if is_prime(temp):
            if singi(temp):
                print(temp)
        
n = int(input())
if n == 1:
    for i in [2,3,5,7]:
        print(i)
    exit()
for i in [2,3,5,7]:
    singi(i)