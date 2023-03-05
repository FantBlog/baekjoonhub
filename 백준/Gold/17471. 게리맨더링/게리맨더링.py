from collections import deque

def DFS_1(now):
    for next in graph[now]:
        if next in team_1 and not next in vis_1:
            vis_1.add(next)
            DFS_1(next)

def DFS_2(now):
    for next in graph[now]:
        if next in team_2 and not next in vis_2:
            vis_2.add(next)
            DFS_2(next)

N = int(input())
people = [0] + list(map(int,input().split()))
graph = [list() for _ in range(N+1)]

for idx in range(1,N+1):
    num, *arr = map(int,input().split())

    for j in range(num):
        graph[idx].append(arr[j])

# print(*graph,sep='\n')

team_1 = deque()
team_2 = deque()
vis_1 = set()
vis_2 = set()
stack_1 = deque()
stack_2 = deque()
bool_1 = False
bool_2 = False
mn = float('inf')

for i in range(1,1<<N-1):
    # print(f'{bin(i)[2:]:0>{N}}')
    for j in range(1,N+1):
        if i & (1<<j-1):
            team_1.append(j)
        else:
            team_2.append(j)
    
    # 모두 이어져 있는지 확인
    stack_1.append(team_1[0])
    vis_1.add(team_1[0])

    DFS_1(stack_1.pop())
    if len(vis_1) == len(team_1):
        bool_1 = True


    stack_2.append(team_2[0])
    vis_2.add(team_2[0])

    DFS_2(stack_2.pop())

    if len(vis_2) == len(team_2):
        bool_2 = True

    # 이어져 있으면 인구 확인
    if bool_1 and bool_2:
        peo_1 = sum(people[j] for j in team_1)
        peo_2 = sum(people[j] for j in team_2)
        # print(peo_1,peo_2)
        if mn > abs(peo_1 - peo_2):
            mn = abs(peo_1 - peo_2)

    team_1.clear()
    vis_1.clear()
    stack_1.clear()
    team_2.clear()
    vis_2.clear()
    stack_2.clear()
    bool_1 = False
    bool_2 = False

if mn == float('inf'):
    print(-1)
else:
    print(mn)