n = int(input())
nums = list(map(int,input().split()))
dp = [1] * n
dp_list = [[nums[i]] for i in range(n)]
for i in range(1,n):
    for j in range(i):
        if nums[i] > nums[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            dp_list[i].append(nums[j])
result = []
idx = n
s = []
for i in range(max(dp),0,-1):
    for j in range(idx-1,-1,-1):
        if dp[j] == i:
            s.append(nums[j])
            idx = j
            break

print(max(dp))
print(*sorted(s))