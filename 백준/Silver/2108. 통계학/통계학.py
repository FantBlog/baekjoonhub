import sys
from collections import Counter
from collections import deque
input = sys.stdin.readline
n = int(input())
result = []
for _ in range(n):
    result.append(int(input()))
result.sort()
print(round(sum(result)/len(result)))
print(result[len(result)//2])

if len(result) < 2:
    print(result[0])
else:
    bin_list = Counter(result).most_common(2)
    if bin_list[0][1] == bin_list[1][1]:
        print(bin_list[1][0])
    else:
        print(bin_list[0][0])

print(max(result)-min(result))