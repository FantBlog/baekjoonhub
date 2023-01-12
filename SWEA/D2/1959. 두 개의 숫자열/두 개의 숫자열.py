T = int(input())

for test_case in range(1, 10+1):
    result = 0
    leng = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    if len(A)>len(B):
        rep = len(B)
        for p in range(len(A) - len(B) + 1):
            temp = 0
            for i in range(rep):
                temp += A[i+p] * B[i]
            if result < temp:
                result = temp
    else:
        rep = len(A)
        for p in range(len(B) - len(A) + 1):
            temp = 0
            for i in range(rep):
                temp += A[i] * B[i+p]
            if result < temp:
                result = temp

    print(f'#{test_case} {result}')