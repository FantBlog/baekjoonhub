from collections import deque
def nm(n,mm):
    if mm == 0:
        result_list = tuple([nums[j] for j in visited])
        if result_list not in print_list:
            print(*result_list)
            print_list.add(result_list)
        return
    for i in range(len(nums)):
        if len(visited) > 0:
            if i >= visited[-1]:
                visited.append(i)   
                nm(n,mm-1)
                visited.pop()
        else:
            visited.append(i)   
            nm(n,mm-1)
            visited.pop()
    
n, m = map(int,input().split())
nums = sorted(list(map(int,input().split())))
visited = deque()
print_list = set()
nm(n,m)