import sys
def input(): return sys.stdin.readline().rstrip()
def VLR(node):
    if not tree.get(node):
        return
    
    print(node,end='')
    VLR(tree[node][0])
    VLR(tree[node][1])

def LVR(node):
    if not tree.get(node):
        return
    
    LVR(tree[node][0])
    print(node,end='')
    LVR(tree[node][1])

def LRV(node):
    if not tree.get(node):
        return
    
    LRV(tree[node][0])
    LRV(tree[node][1])
    print(node,end='')

tree = {}
N = int(input())
for _ in range(N):
    start, left, right = input().split()
    tree[start] = (left,right)


VLR('A')
print()
LVR('A')
print()
LRV('A')