import sys
def input(): return sys.stdin.readline().rstrip()

D, N = map(int,input().split()) # 오븐, 반죽
oven = list(map(int,input().split()))
dou = list(map(int,input().split()))

for idx in range(1, D):
    if oven[idx-1] < oven[idx]:
        oven[idx] = oven[idx-1]
    
start = 0
result = D
for idx in reversed(range(D)):
    if start < N and oven[idx] >= dou[start]:
        result = idx + 1
        start += 1

if start == N:
    print(result)
else:
    print(0)