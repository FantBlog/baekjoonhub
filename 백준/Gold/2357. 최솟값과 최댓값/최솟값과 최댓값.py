import sys
def input(): return sys.stdin.readline().rstrip()

def seg(idx, start, end):
    if start == end:
        tree[idx] = nums[start],nums[start]
        return tree[idx]
    
    a = seg(idx*2 , start , (start+end)//2)
    b = seg(idx*2+1, (start+end)//2 + 1 , end)

    tree[idx] = min(a[0], b[0]), max(a[1], b[1])
    
    return tree[idx]

def p_sum(left, right , idx, start, end):
    if end < left or right < start:
        return float('inf'), 0

    if start >= left and right >= end:
        return tree[idx]

    a = p_sum(left, right , idx*2 , start , (start+end)//2)
    b = p_sum(left, right , idx*2+1, (start+end)//2 + 1 , end)

    return min(a[0], b[0]), max(a[1], b[1])


N, M = map(int,input().split()) # 수 개수, 찾는 횟수
nums = [float('inf')] + [int(input()) for _ in range(N)]

for i in range(N):
    if 2**i >= N:
        break

tree = [float('inf')] * (2**(i+1))
seg(1,1,N)

for _ in range(M):
    a, b = map(int,input().split())
    print(*p_sum(a, b, 1, 1, N))