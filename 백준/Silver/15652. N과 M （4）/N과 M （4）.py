def nm(start,n,m,text=[]):
    if m == 1:
        for i in range(start,n+1):
            print(*text,i)
        return
    for i in range(start,n+1):
        nxt = text + [i]
        nm(i,n,m-1,nxt)
    return 

n,m = map(int,input().split())
nm(1,n,m)