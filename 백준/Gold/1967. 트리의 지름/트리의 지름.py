import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(20_000)

def DFS(start):
    global total
    global mx
    global mx_idx

    if all(tree[start][i][0] in vis for i in range(len(tree[start]))):
        if mx < total:
            mx = total
            mx_idx = start
        return

    for next, val in tree[start]:
        if next not in vis:
            total += val
            vis.add(next)
            DFS(next)
            vis.remove(next)
            total -= val


N = int(input()) # 노드의 개수

if N == 1:
    print(0)
    exit()
    
tree = {}

for _ in range(N-1):
    parent, child, val = map(int,input().split())
    tree.setdefault(parent,[])
    tree[parent].append((child,val))
    
    tree.setdefault(child,[])
    tree[child].append((parent,val))

vis = set()
vis.add(1)
total = 0
mx = -1
mx_idx = 0

DFS(1)
next = mx_idx

vis = set()
vis.add(next)
total = 0
mx = -1
mx_idx = 0

DFS(next)

print(mx)