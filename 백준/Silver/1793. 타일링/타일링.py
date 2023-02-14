import sys
fb = {0:1,1:1}
n = sys.stdin.readlines()

for j in n:
    num = int(j.rstrip('\n'))
    if num < 2:
        fb[num]
    for i in range(2,num+1):
        fb[i] = fb[i-1] + 2 * fb[i-2]
    print(fb[num])