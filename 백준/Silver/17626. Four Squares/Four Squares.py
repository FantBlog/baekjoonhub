import sys
input = sys.stdin.readline
nums = {1:1,2:2,3:3}
num = int(input())
if nums.get(num) == None:
    for temp in range(len(nums),num+1):
        if temp == int(temp**0.5)*(temp**0.5):
            nums[temp] = 1
            continue
        i = 1
        po = []
        while i**2 <= temp:
            b = 3
            b = nums[temp - i**2]
            po.append(b+1)
            i += 1
            if b == 1:
                break
        nums[temp] = min(po)
print(nums[num])