def GCP(a, b):
    if b == 0:
        return a
    return GCP(b, a % b)

for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    GNC = int(M * N / GCP(M, N))

    result = -1

    X = set()
    for i in range(GNC):
        if M * i + x > GNC:
            break
        X.add(M * i + x)

    for i in range(GNC):
        if N * i + y > GNC:
            break
        if N * i + y in X:
            result = N * i + y
            break

    print(result)