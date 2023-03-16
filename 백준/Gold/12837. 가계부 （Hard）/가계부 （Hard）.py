import sys
def input(): return sys.stdin.readline().rstrip()

def change(target, diff , idx, start, end):
    if end < target or target < start:
        return
    
    tree[idx] += diff
    if start != end:
        change(target, diff , idx*2 , start , (start+end)//2)
        change(target, diff , idx*2+1, (start+end)//2 + 1 , end)

def p_sum(left, right, idx, start, end):
    if end < left or right < start:
        return 0

    if start >= left and right >= end:
        return tree[idx]

    return p_sum(left, right , idx*2, start, (start+end)//2) + p_sum(left, right , idx*2 + 1 , (start+end)//2 + 1, end)

N, M = map(int,input().split())

for i in range(N):
    if 2**i >= N:
        break

tree = [0] * (2**(i+1))

for _ in range(M):
    order = list(map(int,input().split()))
    if order[0] == 2:
        print(p_sum(order[1], order[2], 1, 1, N))
    else:
        diff = order[2]
        change(order[1], diff, 1, 1, N)