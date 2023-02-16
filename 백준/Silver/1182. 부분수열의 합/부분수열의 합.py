def f2(i, k, total):
    global count
    if i == k:
        if total == S and max(bits):
            count += 1
        return
    bits[i] = 0
    f2(i + 1, k, total)

    bits[i] = 1
    f2(i + 1, k, total + A[i])

N , S = map(int,input().split())
A = list(map(int,input().split()))
bits = [0] * N
count = 0
f2(0, N, 0)
print(count)