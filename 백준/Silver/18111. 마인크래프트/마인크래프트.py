import sys
from collections import deque

input = sys.stdin.readline
N, M, Block = map(int,input().split())
world = list()
for _ in range(N):
    world.extend(map(int,input().split()))

size = N * M
result_time = -1
for h in range(min(world),max(world) + 1):
    h_block = Block
    time_count = 0
    for i in range(size): # h 높이로 평탄화
        if world[i] > h:
            time_count += (world[i] - h) * 2
            h_block += (world[i] - h)
        elif world[i] < h:
            time_count += (h - world[i])
            h_block -= (h - world[i])
    if result_time == -1:
        result_time = time_count
        result_h = h
    elif time_count <= result_time and h_block >= 0:
        result_time = time_count
        result_h = h
print(result_time, result_h)