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
        
        if lp < len(left) and rp < len(right) and left[lp] < right[rp]:
            result.append(right[rp])
            dct[right[rp]] -= len(left) - lp
            rp += 1
        elif lp < len(left):
            result.append(left[lp])
            lp += 1
        else:
            result.append(right[rp])
            rp += 1
    
    tree[idx] = result
    return tree[idx]

N = int(input())
nums = [0] * (N + 1)
dct = dict()
mx = 0

for i in range(1, N+1):
    temp = int(input())
    dct[temp] = i
    nums[i] = temp
    if mx < temp:
        mx = temp

for i in range(N):
    if 2**i >= N:
        break

tree = [0] * (2**(i+1))

seg(1,1,N)
for i in range(1,N+1):
    print(dct[nums[i]])