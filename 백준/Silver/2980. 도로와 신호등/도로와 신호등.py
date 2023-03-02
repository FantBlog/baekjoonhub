N, L = map(int,input().split())
time = 0
now = 0
for _ in range(N):
    D,R,G = map(int,input().split())
    if now < D:
        time += D - now
        now += D - now
    while time % (R+G) < R:
        time += 1
time += L - now
print(time)