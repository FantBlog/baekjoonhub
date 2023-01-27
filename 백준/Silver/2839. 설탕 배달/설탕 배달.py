N = int(input())
# for N in range(21):
#     print(N, end=' ')
if N == 4:
    print('-1')
elif N < 3:
    print('-1')
else:
    count = N // 5
    N = N % 5
    if N == 0:
        print(count)
    elif N == 3:
        print(count + 1)
    elif N == 1:
        print(count + 1)
    elif N == 4:
        print(count + 2)
    elif N == 2 and count >= 2:
        print(count + 2)
    else:
        print('-1')