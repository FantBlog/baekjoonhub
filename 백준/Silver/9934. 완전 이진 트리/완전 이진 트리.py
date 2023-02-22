import sys
def input(): return sys.stdin.readline().rstrip()

def LVR(N):
    global cnt
    if N >= 2**K:
        return
    
    if node[N] == 0:
        LVR(N*2)
        node[N] = travel[cnt]
        cnt+=1
        LVR(N*2+1)

K = int(input())
travel = list(map(int,input().split()))

node = [0]*(2**K)
cnt = 0

LVR(1)

idx = 1
for i in range(K):
    for j in range(2**i):
        print(node[idx],end=' ')
        idx += 1
    print()