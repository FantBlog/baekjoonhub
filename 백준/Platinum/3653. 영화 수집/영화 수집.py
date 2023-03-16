import sys
def input(): return sys.stdin.readline().rstrip()

def seg(idx, start, end):
    if start == end:
        tree[idx] = nums[start]
        return tree[idx]

    tree[idx] = seg(idx*2 , start , (start+end)//2) + seg(idx*2+1, (start+end)//2 + 1 , end)
    return tree[idx]

def change(target, diff , idx, start, end):
    if end < target or target < start:
        return 

    tree[idx] += diff
    if start != end:
        change(target, diff , idx*2 , start , (start+end)//2)
        change(target, diff , idx*2+1, (start+end)//2 + 1 , end)

def p_sum(left, right , idx, start, end):
    if end < left or right < start:
        return 0

    if start >= left and right >= end:
        return tree[idx]

    return p_sum(left, right , idx*2, start, (start+end)//2) + p_sum(left, right , idx*2 + 1 , (start+end)//2 + 1, end)

for _ in range(int(input())):
    N, M = map(int,input().split()) # 수, 변경 횟수
    nums = [0] * (M+1) + [1] * N
    orders = list(map(int,input().split()))
    dct = dict()

    for i in range(1,N+1):
        dct[i] = M + i
    
    for i in range(N+M):
        if 2**i >= N+M:
            break
    
    tree = [0] * (2**(i+1))
    seg(1,1,N+M)
    
    for i in range(M):
        print(p_sum(0, dct[orders[i]] - 1, 1, 1, N+M), end=' ')
        change(dct[orders[i]], -1 , 1, 1, N+M)
        change(M - i, 1 , 1, 1, N+M)
        dct[orders[i]] = M - i
    print()