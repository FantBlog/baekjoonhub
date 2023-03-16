import sys
def input(): return sys.stdin.readline().rstrip()

def seg(idx, start, end):
    if start == end:
        tree[idx] = nums[start]
        return tree[idx]

    l = seg(idx*2 , start , (start+end)//2)
    r = seg(idx*2+1, (start+end)//2 + 1 , end)
    tree[idx] = [l[0] + r[0], l[1] + r[1]]
    return tree[idx]

def change(target, diff , idx, start, end):
    if end < target or target < start:
        return 

    tree[idx] = [tree[idx][0] + diff[0], tree[idx][1] + diff[1]]
    if start != end:
        change(target, diff , idx*2 , start , (start+end)//2)
        change(target, diff , idx*2+1, (start+end)//2 + 1 , end)

def jj_sum(left, right , idx, start, end):
    if end < left or right < start:
        return 0

    if start >= left and right >= end:
        return tree[idx][1]
    
    return jj_sum(left, right , idx*2, start, (start+end)//2) + jj_sum(left, right , idx*2 + 1 , (start+end)//2 + 1, end)

def hh_sum(left, right , idx, start, end):
    if end < left or right < start:
        return 0

    if start >= left and right >= end:
        return tree[idx][0]
    
    return hh_sum(left, right , idx*2, start, (start+end)//2) + hh_sum(left, right , idx*2 + 1 , (start+end)//2 + 1, end)


N = int(input())
inp = list(map(int,input().split()))
nums = [0] * (N + 1)
for i in range(N):
    if inp[i] % 2:
        nums[i + 1] = [1, 0] # 홀, 짝
    else:
        nums[i + 1] = [0, 1]

M = int(input())

for i in range(N+M):
    if 2**i >= N+M:
        break

tree = [0] * (2**(i+1))
seg(1,1,N)

for i in range(M):
    order, *text = map(int,input().split())
    if order == 1:
        if nums[text[0]][1] and text[1] % 2: # 짝인데 홀수
            nums[text[0]] = [1, 0]
            change(text[0], [1,-1], 1, 1, N)
        elif nums[text[0]][0] and text[1] % 2 == 0:
            nums[text[0]] = [0, 1]
            change(text[0], [-1,1], 1, 1, N)
    elif order == 2:
        print(jj_sum(text[0], text[1], 1, 1, N))
    else:
        print(hh_sum(text[0], text[1], 1, 1, N))