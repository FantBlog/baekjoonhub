import sys
def input(): return sys.stdin.readline().rstrip()

def seg(idx, start, end):
    if start == end:
        tree[idx] = nums[start]
        return tree[idx]

    tree[idx] = min(seg(idx*2 , start , (start+end)//2), seg(idx*2+1, (start+end)//2 + 1 , end))
    return tree[idx]

def p_sum(left, right , idx, start, end):
    if end < left or right < start:
        return float('inf')

    if start >= left and right >= end:
        return tree[idx]

    return min(p_sum(left, right , idx*2, start, (start+end)//2), p_sum(left, right , idx*2 + 1 , (start+end)//2 + 1, end))


N, M = map(int,input().split()) # 수 개수, 찾는 횟수
nums = [float('inf')] + [int(input()) for _ in range(N)]

for i in range(N):
    if 2**i >= N:
        break

tree = [float('inf')] * (2**(i+1))
seg(1,1,N)

for _ in range(M):
    a, b = map(int,input().split())
    print(p_sum(a, b, 1, 1, N))