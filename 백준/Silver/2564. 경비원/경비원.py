def move_clock(x,y,dong,store,count):
    if dong[0] == 1:
        while dong[1] != x:
            if dong == store:
                return [0,0],count
            count += 1
            dong[1] += 1
        return [4,0],count
    if dong[0] == 2:
        while dong[1] != 0:
            if dong == store:
                return [0,0],count
            count += 1
            dong[1] -= 1
        return [3,y],count
    if dong[0] == 3:
        while dong[1] != 0:
            if dong == store:
                return [0,0],count
            count += 1
            dong[1] -= 1
        return [1,0],count
    if dong[0] == 4:
        while dong[1] != y:
            if dong == store:
                return [0,0],count
            count += 1
            dong[1] += 1
        return [2,x],count
def move_reverse_clock(x,y,dong,store,count):
    if dong[0] == 1:
        while dong[1] != 0:
            if dong == store:
                return [0,0],count
            count += 1
            dong[1] -= 1
        return [3,0],count
    if dong[0] == 2:
        while dong[1] != x:
            if dong == store:
                return [0,0],count
            count += 1
            dong[1] += 1
        return [4,y],count
    if dong[0] == 3:
        while dong[1] != y:
            if dong == store:
                return [0,0],count
            count += 1
            dong[1] += 1
        return [2,0],count
    if dong[0] == 4:
        while dong[1] != 0:
            if dong == store:
                return [0,0],count
            count += 1
            dong[1] -= 1
        return [1,x],count
x,y = map(int,input().split())
t = int(input())
store = list()
for i in range(t):
    store.append(list(map(int,input().split())))
dong = list(map(int,input().split()))
total = 0
for sto in store:
    result = []
    count = 0 
    temp = dong[:]
    while temp[0] != 0:
        temp,count = move_clock(x,y,temp,sto,count)
    result.append(count)
    temp = dong[:]
    count = 0 
    while temp[0] != 0:
        temp,count = move_reverse_clock(x,y,temp,sto,count)
    result.append(count)
    total += min(result)
print(total)