import sys
n = int(sys.stdin.readline())
count_list = [0]*10001
for _ in range(n):
    a = int(sys.stdin.readline())
    count_list[a] += 1
    
for i in range(1,10001):
    for _ in range(count_list[i]):
        print(i)