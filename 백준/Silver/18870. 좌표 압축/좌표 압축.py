import sys
input = sys.stdin.readline

def quiq(arr):
    start = 0
    end = len(arr)
    if end < 2:
        return arr
    center = (start + end) // 2
    left = []
    right = []
    same = []
    pivot = arr[center]
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            same.append(x)
    return quiq(left) + same + quiq(right)
n = int(input())
arr = list(map(int,input().split()))

sort_arr = quiq(list(set(arr)))

result = dict()
for idx,x in enumerate(sort_arr):
    result[x] = idx

for x in arr:
    print(result[x],end=' ')