def push1D(x):
    
    pan1D[x] += 1
    # 가로
    # 몫이 같은애들 +1
    dx = x + 1
    while dx // N == x // N:
        pan1D[dx] += 1
        dx += 1
        
    dx = x - 1
    while dx // N == x // N:
        pan1D[dx] += 1
        dx -= 1

    # 세로
    # + n 만큼 + 1

    dx = x + N
    while 0 <= dx < N*N:
        pan1D[dx] += 1
        dx += N
        
    dx = x - N
    while 0 <= dx < N*N:
        pan1D[dx] += 1
        dx -= N
    
    # 대각선
    # n+1,n-1 만큼 차이

    dx = x + N + 1
    while 0 <= dx < N*N:
        if abs(dx//N - (dx-(N+1))//N) != 1:
            break
        pan1D[dx] += 1
        dx += N + 1
        
    dx = x - (N + 1)
    while 0 <= dx < N*N:
        if abs(dx//N - (dx+(N+1))//N) != 1:
            break
        pan1D[dx] += 1
        dx -= (N + 1)
    
    dx = x
    while 0 <= dx+(N-1) < N*N:
        if dx//N == (dx+(N-1))//N:
            break
        dx += (N-1)
        pan1D[dx] += 1
        
    dx = x
    while 0 <= dx-(N-1) < N*N:
        if dx//N == (dx-(N-1))//N:
            break
        dx -= (N-1)
        pan1D[dx] += 1
        


def pop1D(x):
    pan1D[x] -= 1
    # 가로
    # 몫이 같은애들 +1
    dx = x + 1
    while dx // N == x // N:
        pan1D[dx] -= 1
        dx += 1
        
    dx = x - 1
    while dx // N == x // N:
        pan1D[dx] -= 1
        dx -= 1

    # 세로
    # + n 만큼 + 1

    dx = x + N
    while 0 <= dx < N*N:
        pan1D[dx] -= 1
        dx += N
        
    dx = x - N
    while 0 <= dx < N*N:
        pan1D[dx] -= 1
        dx -= N
    
    # 대각선
    # n+1,n-1 만큼 차이

    dx = x + N + 1
    while 0 <= dx < N*N:
        if abs(dx//N - (dx-(N+1))//N) != 1:
            break
        pan1D[dx] -= 1
        dx += N + 1
        
    dx = x - (N + 1)
    while 0 <= dx < N*N:
        if abs(dx//N - (dx+(N+1))//N) != 1:
            break
        pan1D[dx] -= 1
        dx -= (N + 1)
    
    dx = x
    while 0 <= dx+N-1 < N*N:
        if dx//N == (dx+N-1)//N:
            break
        dx += N - 1
        pan1D[dx] -= 1
        
    dx = x
    while 0 <= dx-(N-1) < N*N:
        if dx//N == (dx-(N-1))//N:
            break
        dx -= N - 1
        pan1D[dx] -= 1

def queen1D(i):
    global count

    if i == N:
        count += 1
        # print(result)
        return
    
    for x in range(N*i, N*(i+1)):
        if pan1D[x] == 0:
            pnt.append(x)
            push1D(x)
            queen1D(i+1)
            pnt.pop()
            pop1D(x)


N = int(input())
pan1D = [0]*N*N
pnt = []
count = 0
queen1D(0)
print(count)