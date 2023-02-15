def nm(n,m):
    if m == 0:
        print(*visited)
        return
    for i in range(1,n+1):
        if i not in visited:
            visited.append(i)
            nm(n,m-1)
            visited.pop()
    
n, m = map(int,input().split())
visited = []
result = []
nm(n,m)