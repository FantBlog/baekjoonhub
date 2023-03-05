from collections import deque
import copy

def rotation(arr,rr,cc,D):
    rr -= 1
    cc -= 1

    for i in range(1,D+1):
        Rm, Rn = rr + i , rr - i
        Cm, Cn = cc + i , cc - i 

        r = rr - i
        c = cc - i

        r += 1
        while r <= Rm:
            arr[r][c], arr[r-1][c] = arr[r-1][c], arr[r][c]
            r += 1
        r -= 1

        c += 1
        while c <= Cm:
            arr[r][c], arr[r][c-1] = arr[r][c-1], arr[r][c]
            c += 1
        c -= 1

        r -= 1
        while r > Rn - 1:
            arr[r][c], arr[r+1][c] = arr[r+1][c], arr[r][c]
            r -= 1
        r += 1

        c -= 1
        while c > Cn:
            arr[r][c], arr[r][c+1] = arr[r][c+1], arr[r][c]
            c -= 1
        c += 1

    return arr

def minarr():
    newarr = copy.deepcopy(arr)

    # print(johap)
    for idx in johap:
        # print(*newarr,sep='\n',end='\n\n')
        newarr = rotation(newarr,*rot_list[idx])
    # print(*newarr,sep='\n',end='\n\n')
    
    mn = float('inf')
    for r in range(R):
        temp = sum(newarr[r])
        if mn > temp:
            mn = temp

    return mn

def com(deeps):
    global mn

    if deeps == N:
        # print(johap)
        temp = minarr()
        if mn > temp:
            mn = temp
        
        return
    
    for i in range(N):
        if i not in johap:
            johap.append(i)
            com(deeps + 1)
            johap.pop()

R, C, N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(R)]

rot_list = [list(map(int,input().split())) for _ in range(N)]

mn = float('inf')
johap = []

com(0)

print(mn)