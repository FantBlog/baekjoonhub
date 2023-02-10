import sys
a,b = map(int,sys.stdin.readline().rstrip('\n').split())
num_list = [i for i in range(b+1)]
prime_list = [True]*(b+1)
prime_list[0] = False
prime_list[1] = False
for i in range(2,int(b**0.5)+1):
    if prime_list[i]:
        for j in range(i*2,b+1,i):
            prime_list[j] = False
for i in range(a,b+1):
    if prime_list[i]:
        print(num_list[i])