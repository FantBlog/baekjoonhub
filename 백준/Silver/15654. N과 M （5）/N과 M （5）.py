def nm(n,m):
    if m == 0:
        print(*visited)
        return
    for i in nums:
        if i not in visited:
            visited.append(i)
            nm(n,m-1)
            visited.pop()
    
n, m = map(int,input().split())
nums = sorted(list(map(int,input().split())))
visited = []
result = []
nm(n,m)