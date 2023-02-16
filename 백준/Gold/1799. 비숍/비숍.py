def bs_push(x):
    check_pan[x] += 1

    dx = x + N + 1
    while 0 <= dx < N*N:
        if abs(dx//N - (dx-(N+1))//N) != 1:
            break
        check_pan[dx] += 1
        dx += N + 1
        
    dx = x - (N + 1)
    while 0 <= dx < N*N:
        if abs(dx//N - (dx+(N+1))//N) != 1:
            break
        check_pan[dx] += 1
        dx -= (N + 1)
    
    dx = x
    while 0 <= dx+(N-1) < N*N:
        if dx//N == (dx+(N-1))//N:
            break
        dx += (N-1)
        check_pan[dx] += 1
        
    dx = x
    while 0 <= dx-(N-1) < N*N:
        if dx//N == (dx-(N-1))//N:
            break
        dx -= (N-1)
        check_pan[dx] += 1
        


def bs_pop(x):
    check_pan[x] -= 1

    dx = x + N + 1 
    while 0 <= dx < N*N:
        if abs(dx//N - (dx-(N+1))//N) != 1:
            break
        check_pan[dx] -= 1
        dx += N + 1
        
    dx = x - (N + 1)
    while 0 <= dx < N*N:
        if abs(dx//N - (dx+(N+1))//N) != 1:
            break
        check_pan[dx] -= 1
        dx -= (N + 1)
    
    dx = x
    while 0 <= dx+N-1 < N*N:
        if dx//N == (dx+N-1)//N:
            break
        dx += N - 1
        check_pan[dx] -= 1
        
    dx = x 
    while 0 <= dx-(N-1) < N*N:
        if dx//N == (dx-(N-1))//N:
            break
        dx -= N - 1
        check_pan[dx] -= 1

def bishop(i):
    global mx
    global count

    if count > mx:
        mx = count

    if i > end:
        return
    
    for x in search[i]:
        if pan1D[x] == 1 and check_pan[x] == 0:
            bs_push(x)
            count += 1
            bishop(i+2)
            count -= 1
            bs_pop(x)

        elif check_pan[x] == 0:
            bishop(i+2)

def bishop2(i):
    global mx2
    global count

    if count > mx2:
        mx2 = count

    if i >= end:
        return
    
    for x in search[i]:
        if pan1D[x] == 1 and check_pan[x] == 0:
            bs_push(x)
            count += 1
            bishop2(i+2)
            count -= 1
            bs_pop(x)

        elif check_pan[x] == 0:
            bishop2(i+2)


N = int(input())
pan1D = []
for _ in range(N):
    pan1D += list(map(int,input().split()))

search = [[] for _ in range(2*N-1)]
x = 0
i = 0
search[i].append(x)
while x < N-1:
    i += 1
    x += 1
    search[i].append(x)
    y = x
    while y < N*N:
        if ( y +  N - 1 ) // N == y // N:
            break
        y += N-1
        search[i].append( y )
x = N - 1
while x + N < N*N:
    i += 1
    x += N
    search[i].append(x)
    y = x
    while y + N - 1 < N*N:
        if ( y +  N - 1 ) // N == y // N:
            break
        y += N-1
        search[i].append( y )

check_pan = [0]*N*N

end = len(search)

count = 0

mx = 0
bishop(0)

count = 0
mx2 = 0
bishop2(1)

print(mx+mx2)