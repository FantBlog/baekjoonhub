import sys
def input(): return sys.stdin.readline().rstrip()

def seg(idx, start, end):
    if start == end:
        tree[idx] = nums[start]
        return tree[idx]

    tree[idx] = seg(idx*2 , start , (start+end)//2) * seg(idx*2+1, (start+end)//2 + 1 , end)
    return tree[idx]

def change(target, diff , idx, start, end , num):
    if end < target or target < start:
        return tree[idx]

    
    if start != end:
        a = change(target, diff , idx*2 , start , (start+end)//2, num)
        b = change(target, diff , idx*2+1, (start+end)//2 + 1 , end , num)
        tree[idx] = a * b
        return tree[idx]
    else:
        tree[idx] = num
        return tree[idx]

def p_sum(left, right , idx, start, end):
    if end < left or right < start:
        return 1

    if start >= left and right >= end:
        return tree[idx]
 
    return p_sum(left, right , idx*2, start, (start+end)//2) * p_sum(left, right , idx*2 + 1 , (start+end)//2 + 1, end)


while True:
    try:
        N, K = map(int,input().split()) # 수, 변경 횟수, 구간 합 횟수
        nums = [0] * (N + 1)
        inp = list(map(int,input().split()))

        for i in range(N):
            if inp[i] > 0:
                nums[i+1] = 1
            elif inp[i] < 0:
                nums[i+1] = -1
            else:
                nums[i+1] = 0

        for i in range(N):
            if 2**i >= N:
                break

        tree = [0] * (2**(i+1))
        seg(1,1,N)

        for _ in range(K):
            order, b, c = input().split()

            b = int(b)
            c = int(c)

            if order == 'C':
                if c > 0:
                    c = 1
                elif c < 0:
                    c = -1
                else:
                    c = 0
                
                if nums[b]:
                    diff = c / nums[b]
                else:
                    diff = c

                nums[b] = c
                
                change(b,diff,1,1,N, c)

            else:
                result = p_sum(b,c,1,1,N)
                if result > 0:
                    print('+',end='')
                elif result == 0:
                    print('0',end='')
                else:
                    print('-',end='')

        print()
    except:
        exit()