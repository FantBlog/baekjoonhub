import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(20_000)

def sort_tree(josang,start,end):
    if start >= N or start > end:
        return
    for idx in range(start+1,end+1):
        if nums[idx] > nums[start]:
            break
    else:
        idx = end + 1
    sort_tree(josang*2,start+1,idx-1)
    sort_tree(josang*2+1,idx,end)
    print(nums[start])

nums = list(map(int,sys.stdin.readlines()))
N = len(nums)
sort_tree(1,0,N-1)