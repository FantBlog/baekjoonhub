import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

# 13335번 트럭
n,w,l = map(int,input().split()) # 트럭수, 길이, 무게제한
truck = deque(map(int,input().split()))
dari = deque()
time = 0

for _ in range(w):
    dari.append(0)

while truck:

    if sum(dari) - dari[0] + truck[0] <= l: # 무게 감당되면
        dari.popleft()
        dari.append(truck.popleft())
        time += 1

    else:
        if dari[0] != 0:
            dari.popleft()
            dari.append(0)
        else:
            dari.append(dari.popleft())
        time += 1
time += w

print(time)