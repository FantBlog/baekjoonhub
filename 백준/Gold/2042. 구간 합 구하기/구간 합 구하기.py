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


N, M, K = map(int,input().split()) # 수, 변경 횟수, 구간 합 횟수
nums = [0] + [int(input()) for _ in range(N)]
for i in range(N):
    if 2**i >= N:
        break
tree = [0] * (2**(i+1))
seg(1,1,N)
for _ in range(M+K):
    a, b, c = map(int,input().split())
    if a == 1:
        diff = c - nums[b]
        nums[b] = c
        change(b,diff,1,1,N)
    else:
        print(p_sum(b,c,1,1,N))