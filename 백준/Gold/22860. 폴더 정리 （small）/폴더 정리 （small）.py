import sys
sys.setrecursionlimit(10**5)

def DFS(sub):
    global count
    total = folder[sub]
    for a in total:
        if a[1] == 1:
            DFS(a[0])
        else:
            if not a[0] in visited:
                visited.add(a[0])
            count = count + 1


N, M = map(int, input().split())

folder = dict()
folder['main'] = set()

for _ in range(N + M):
    P, F, C = input().split()
    folder.setdefault(P, set())

    if C == '1':
        folder[P].add((F, 1))
        folder.setdefault(F, set())
    else:
        folder[P].add((F, 0))

K = int(input())

for _ in range(K):
    find = input().split('/')
    
    visited = set()
    count = 0

    DFS(find[-1])

    print(len(visited), count)