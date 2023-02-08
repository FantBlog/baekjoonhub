import sys
input = sys.stdin.readline
n = int(input())
ssang = int(input())
com_list = set()
vilus = {1:True}
vi_list = []
for _ in range(ssang):
    com_list.add(tuple(map(int,input().split())))
com_list = sorted(com_list,key=lambda x:x[0])
count = 1
while count:
    count = 0
    for com in com_list: # 컴퓨터 리스트
        for key in vilus: # 감염된 컴퓨터
            if key in com: # 연결되어있다면
                for co in com:
                    if vilus.get(co):
                        continue
                    else:
                        vi_list.append(co) # 감염시킬 리스트
                        count += 1
    for co in vi_list:
        vilus[co] = True # 감염시킴

print(len(vilus)-1)