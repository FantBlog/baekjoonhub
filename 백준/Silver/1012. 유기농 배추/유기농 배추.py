import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def bachu(bat2,o,p,ho,ve):
    bat2[p][o] = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        if 0 <= p+dy[i] < ve and 0 <= o+dx[i] < ho:
            if bat2[p+dy[i]][o+dx[i]] == 1:
                bachu(bat2,o+dx[i],p+dy[i],ho,ve)
    return
t = int(input().rstrip('\n'))
for _ in range(t):
    m, n, k = map(int,input().rstrip('\n').split())
    bat = [[0]*m for _ in range(n)]
    for _ in range(k):
        a, b = map(int,input().rstrip('\n').split())
        bat[b][a] = 1
    # pprint.pprint(bat)
    cnt = 0
    for x in range(m):
        for y in range(n):
            if bat[y][x] == 1:
                bachu(bat,x,y,m,n)
                cnt += 1
    # pprint.pprint(bat)
    print(cnt)