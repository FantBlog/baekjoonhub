import sys
fibo_list = [0,1]
x = 1_000_000
m = 15 * x//10
z = int(sys.stdin.readline()) % m
if z<2:
    print(z)
else:
    for _ in range(2,z):
        fibo_list = [fibo_list[1],sum(fibo_list)%x]
    print(sum(fibo_list)%x)