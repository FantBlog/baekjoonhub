T = int(input())
for t in range(1,T+1):
    a, b = map(int,input().split())
    a = a % 10
    if a:
        if b % 4:
            print(a ** (b%4) % 10)
        else:
            print(a ** 4 % 10)
    else:
        print(10)