import sys
def input(): return sys.stdin.readline().rstrip()

def seg(idx, start, end):
    if start == end:
        tree[idx] = nums[start]
        return tree[idx]

    tree[idx] = seg(idx*2 , start , (start+end)//2) + seg(idx*2+1, (start+end)//2 + 1 , end)
    return tree[idx]

def change(t_start, t_end, diff , idx, start, end):
    if lazy[idx] != 0:
        update_lazy(idx, start, end)
        
    if end < t_start or t_end < start:
        return
    
    if start >= t_start and t_end >= end:
        # 종료
        tree[idx] = end - start + 1 - tree[idx]
        if start != end:
            lazy[idx * 2] += diff
            lazy[idx * 2 + 1] += diff
        return
    
    if start != end:
        change(t_start, t_end, diff , idx*2 , start , (start+end)//2)
        change(t_start, t_end, diff , idx*2+1, (start+end)//2 + 1 , end)
        tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]

def p_sum(left, right , idx, start, end):
    if lazy[idx] != 0:
        update_lazy(idx, start, end)
        
    if end < left or right < start:
        return 0

    if start >= left and right >= end:
        return tree[idx]

    return p_sum(left, right , idx*2, start, (start+end)//2) + p_sum(left, right , idx*2 + 1 , (start+end)//2 + 1, end)

def update_lazy(idx, start, end):
    if lazy[idx] % 2:
        tree[idx] = end - start + 1 - tree[idx]
    if start != end:
        lazy[idx * 2] += lazy[idx]
        lazy[idx * 2 + 1] += lazy[idx]
    lazy[idx] = 0

N, M = map(int,input().split()) # 수, 변경 횟수, 구간 합 횟수
nums = [0] + [0] * N

for i in range(N):
    if 2**i >= N:
        break
    
tree = [0] * (2**(i+1))
lazy = [0] * (2**(i+1))

seg(1, 1, N)

for _ in range(M):
    order, *data = map(int,input().split())
    if order:
        print(p_sum(data[0], data[1], 1, 1, N))
    else:
        change(data[0], data[1], 1, 1, 1, N)