import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
nums = []
for _ in range(N):
    nums.append(list(map(int,input().split())))

for r in range(1,N):
    for i in range(r+1):
        if i == 0:
            nums[r][i] += nums[r-1][i]
        elif i == r:
            nums[r][i] += nums[r-1][i-1]
        else:
            nums[r][i] += max(nums[r-1][i],nums[r-1][i-1])

print(max(nums[N-1]))