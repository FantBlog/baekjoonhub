import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

for _ in range(int(input())):
    N = int(input())

    nums = deque(sorted([input() for _ in range(N)],key=lambda x : len(x)))

    result = 'YES'
    while nums:
        now = nums.popleft()

        for text in nums:
            if len(text) == len(now):
                continue
            if now == text[:len(now)]:
                result = 'NO'
                nums.clear()
                break
    print(result)