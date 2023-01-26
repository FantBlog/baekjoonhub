T = int(input())
for test_case in range(1,T+1):
    a, b = map(int,input().split())
    a = a % 10

    if a > 0:
        if b % 4 > 0:
            print(a ** (b%4) % 10)
        else:
            print(a ** 4 % 10)
    else:
        print(10)