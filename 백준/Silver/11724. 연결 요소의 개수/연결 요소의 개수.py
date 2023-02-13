import sys
from collections import deque
input = sys.stdin.readline

def makeset(tpl):
    result_set = set()
    serch = deque()
    for i in range(2):
        result_set.add(tpl[i])
        serch.append(tpl[i])
    while len(serch) > 0:
        now = serch.popleft()
        for line in line_list:
            if line[0] == now:
                if line[1] not in result_set:
                    result_set.add(line[1])
                    serch.append(line[1])
            if line[1] == now:
                if line[0] not in result_set:
                    result_set.add(line[0])
                    serch.append(line[0])
    return result_set


n, m = map(int,input().split())
if m == 0:
    print(n)
    exit()
line_list = deque()
for i in range(m):
    start, end = map(int,input().split())
    if end > start:
        line_list.append((start,end))
    else:
        line_list.append((end,start))

line_list = deque(sorted(line_list,key=lambda x:x[0]))
set_list = []
while len(line_list) > 0:
    check = line_list.popleft()
    if all(check[i] not in set_list[j] for i in range(2) for j in range(len(set_list))):
        set_list.append(makeset(check))
        
total = 0
for st in set_list:
    total += len(st)
print(n-total+len(set_list))