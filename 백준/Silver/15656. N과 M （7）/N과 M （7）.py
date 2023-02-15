def nm(n,mm):
    if mm == 0:
        print(*visited)
        return
    for i in nums:
        visited.append(i)
        nm(n,mm-1)
        visited.pop()
    
n, m = map(int,input().split())
nums = sorted(list(map(int,input().split())))
visited = []
result = []
nm(n,m)