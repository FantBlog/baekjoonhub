def dfs(start):
    global maze
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    maze[start[1]][start[0]] = 2
    for i in range(4):
        if maze[start[1] + dy[i]][start[0] + dx[i]] == 0:
            stack.append((start[0] + dx[i],start[1] + dy[i]))
        elif maze[start[1] + dy[i]][start[0] + dx[i]] == 3:
            return True
    return False

t = 10
for tc in range(1,t+1):
    tci = int(input())
    size = 100
    maze = [[1]*(size+2)]
    for _ in range(size):
        maze.append([1] + list(map(int,list(input()))) + [1])
    maze.append([1]*(size+2))
    stack = []
    for x in range(size+2):
        for y in range(size+2):
            if maze[y][x] == 2:
                stack.append((x,y))
    result = 0
    while len(stack) > 0:
        if dfs(stack.pop()):
            result = 1
            break
    print(f'#{tc} {result}')