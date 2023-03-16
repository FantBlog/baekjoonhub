import sys
def input(): return sys.stdin.readline().rstrip()

def seg(idx, start, end):
    if start == end:
        tree[idx] = nums[start]
        return tree[idx]

    tree[idx] = min(seg(idx*2 , start , (start+end)//2), seg(idx*2+1, (start+end)//2 + 1 , end), key=lambda x:x[0])
    return tree[idx]

def change(target, diff , idx, start, end):
    if end < target or target < start:
        return 

    if start != end:
        change(target, diff , idx*2 , start , (start+end)//2)
        change(target, diff , idx*2+1, (start+end)//2 + 1 , end)
        tree[idx] = min(tree[idx*2],tree[idx*2+1], key=lambda x:x[0])
        
        
N = int(input())
inp = list(map(int,input().split()))
nums = [0] * (N + 1)
for idx, val in enumerate(inp):
    nums[idx + 1] = [val, idx + 1]

for i in range(N):
    if 2**i >= N:
        break

tree = [0] * (2**(i+1))
seg(1,1,N)

M = int(input())
for _ in range(M):
    order = list(map(int,input().split()))
    if order[0] == 2:
        print(tree[1][1])
    else:
        diff = order[2] - nums[order[1]][0]
        nums[order[1]][0] = order[2]
        change(order[1], diff, 1, 1, N)