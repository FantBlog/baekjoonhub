ans = set()

def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def dfs(v, numbers, visited, tmp, l, k):
    if k == l:
        return
    
    global ans
    visited[v] = 1
    tmp.append(numbers[v])

    now = ''
    for t in tmp:
        now += t
    
    if not now in ans:
        ans.add(now)

    for idx in range(l):
        if not visited[idx]:
            dfs(idx, numbers, visited, tmp, l, k + 1)

    tmp.pop()
    visited[v] = 0

def solution(numbers):
    global ans
    l = len(numbers)

    for i in range(l):
        if numbers[i] != '0':
            visited = [0] * l
            tmp = []
            dfs(i, numbers, visited, tmp, l, 0)

    answer = 0
    for num in ans:
        if is_prime(int(num)):
            print(num)
            answer += 1
    return answer