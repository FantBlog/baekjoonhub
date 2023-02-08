import sys
input = sys.stdin.readline
n = int(input())
stair = []
for _ in range(n):
    stair.append(int(input()))
if n < 2:
    print(stair[0])
    exit()
D = [[0]*2 for _ in range(n)]
D[0][0] += stair[0] # 한칸
D[1][1] += D[0][0] + stair[1] # 한칸
D[1][0] += stair[1] # 시작부터 2칸
for i in range(2,n):
    for j in range(2):
        if j: # 연속 2번째 계단
            D[i][j] = D[i-1][0] + stair[i]
        else: # 처음 밟는 계단
            D[i][j] = max(D[i-2][1],D[i-2][0]) + stair[i]
print(max(D[-1]))