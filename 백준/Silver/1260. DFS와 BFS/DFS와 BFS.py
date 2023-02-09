import sys
from collections import deque
input = sys.stdin.readline
def DFS(lines,num,result):
    serch = []
    for i in range(len(lines)):
        if num == lines[i][0] and lines[i][1] not in result:
            serch.append(lines[i][1])
    
    if len(serch) == 1:
        if serch[0] not in result:
            result.append(serch[0])
        DFS(lines,serch[0],result)
    elif len(serch) > 1:
        serch.sort()
        for i in range(len(serch)):
            if serch[i] not in result:
                result.append(serch[i])
            DFS(lines,serch[i],result)

    return result
    
def BFS(lines,result,serch):

    while len(serch) > 0:
        num = serch.popleft()
        serch_list = []
        for i in range(len(lines)):
            if num == lines[i][0] and lines[i][1] not in result and lines[i][1] not in serch:
                serch_list.append(lines[i][1])
        serch.extend(sorted(serch_list))
        for i in serch:
            if i not in result:
                result.append(i)

    return result

    
n, m, v = map(int,input().split())
lines = []
for _ in range(m):
    a, b = map(int,input().split())
    lines.extend([(a,b),(b,a)])

result = [v]
result_d = DFS(lines,v,result)
print(*result_d)

result = [v]
serch = deque()
serch.append(v)
result_b = BFS(lines,result,serch)
print(*result_b)