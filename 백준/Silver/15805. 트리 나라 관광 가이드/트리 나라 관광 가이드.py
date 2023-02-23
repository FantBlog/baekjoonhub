import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
city = list(map(int,input().split()))
stack = []
dic = {}
for i in city:
    if len(stack) > 1 and stack[-2] == i:
        son = stack.pop()
        mth = stack[-1]
        dic[son] = mth
    else:
        stack.append(i)

print(len(dic) + 1)
for i in range(len(dic) + 1):
    if dic.get(i) == None:
        print(-1,end=' ')
    else:
        print(dic.get(i),end=' ')