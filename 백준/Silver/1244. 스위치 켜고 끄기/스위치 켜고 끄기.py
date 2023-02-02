def switch(list, num_list):
    for i in num_list:
        if list[i-1]:
            list[i-1] = 0
        else:
            list[i-1] = 1
    return list
n = int(input())
switch_status = list(map(int,input().split()))
t = int(input())
for _ in range(t):
    gender , num = map(int,input().split())
    num_list = []
    if gender % 2:
        num_list = [i for i in range(num,n+1,num)]
    else:
        i = 0
        num_list.append(num)
        while True:
            try:
                i += 1
                if num-i <= 0 or num + i > n:
                    break
                if switch_status[num-i-1] == switch_status[num+i-1]:
                    num_list.append(num+i)
                    num_list.insert(0,num-i)
                else:
                    break
            except:
                break
    switch_status = switch(switch_status,num_list)
for i in range(len(switch_status)):
    if i % 20 == 0 and i != 0:
        print()
    print(switch_status[i],end=' ')