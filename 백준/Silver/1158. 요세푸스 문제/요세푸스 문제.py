from collections import deque
N, K = map(int,input().split())
nums = deque([i for i in range (1,N+1)])
result = []
while nums:
    for i in range(K):
        if not nums:
            break
        if K-1 == i:
            result.append(nums.popleft())
        else:
            nums.append(nums.popleft())
print('<',end='')
print(*result,sep=', ',end='')
print('>')