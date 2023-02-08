fib = {0:0,1:1,2:1}
n = int(input())
for _ in range(n):
    num = int(input())
    if num == 0:
        print('1 0')
    elif num == 1:
        print('0 1')
    else:
        for i in range(2,num+1):
            fib[i] = fib[i-1] + fib[i-2]
        print(fib[num-1],fib[num])