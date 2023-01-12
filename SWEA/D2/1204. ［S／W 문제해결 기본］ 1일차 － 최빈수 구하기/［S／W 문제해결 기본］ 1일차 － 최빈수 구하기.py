T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    H = list(map(int, input().split()))
    A = [0] * 101
    for i in range(1000):
        A[100-H[i]] +=1
    print(f"#{test_case} {100-A.index(max(A))}")