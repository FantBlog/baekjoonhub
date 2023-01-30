import sys
a,b = map(int,sys.stdin.readline().rstrip('\n').split())
num_list = [i for i in range(b+1)]
not_prime_list = [True]*(b+1)
for i in range(int(b**0.5)+1):
    if i <= 1:
        not_prime_list[i] = False
    else:
        if not_prime_list[i]:
            for j in num_list[i*2::i]:
                not_prime_list[j] = False
for idx,i in enumerate(not_prime_list):
    if i and idx >= a:
        print(num_list[idx])