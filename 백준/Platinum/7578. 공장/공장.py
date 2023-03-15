import sys
def input(): return sys.stdin.readline().rstrip()

def seg(idx, start, end):
    global cnt
    if start == end:
        tree[idx] = [nums[start]]
        return tree[idx]

    left = seg(idx*2 , start , (start+end)//2)
    right =  seg(idx*2+1, (start+end)//2 + 1 , end)

    result = list()
    lp = 0
    rp = 0

    for _ in range(end - start + 1):
        
        if lp < len(left) and rp < len(right) and dct[left[lp]] > dct[right[rp]]:
            result.append(right[rp])
            rp += 1
            cnt += len(left) - lp
        elif lp < len(left):
            result.append(left[lp])
            lp += 1
        else:
            result.append(right[rp])
            rp += 1
    
    tree[idx] = result
    return tree[idx]

N = int(input())
nums = [0] + list(map(int,input().split()))
dct = dict()
for idx, val in enumerate(list(map(int,input().split()))):
    dct[val] = idx

for i in range(N):
    if 2**i >= N:
        break

tree = [0] + [float('inf')] * (2**(i+1) - 1)

cnt = 0
seg(1,1,N)
print(cnt)