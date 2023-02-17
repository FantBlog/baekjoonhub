from collections import deque

def turn(tob, dirt):
    if dirt == 1:
        tob.appendleft(tob.pop())
    else:
        tob.append(tob.popleft())


tob_1 = deque(map(int,list(input())))
tob_2 = deque(map(int,list(input())))
tob_3 = deque(map(int,list(input())))
tob_4 = deque(map(int,list(input())))

N = int(input())
for _ in range(N):
    num, dirt = map(int,input().split())

    result = [num]

    stack = deque()
    re_stack = deque()
    stack.append(num)
    while True:
        now = stack[0]
        if now + 1 == 2:
            if tob_1[2] != tob_2[6]:
                stack.appendleft(now+1)
                result.append(now+1)
            else:
                break
        elif now + 1 == 3:
            if tob_2[2] != tob_3[6]:
                stack.appendleft(now+1)
                result.append(now+1)
            else:
                break
        elif now + 1 == 4:
            if tob_3[2] != tob_4[6]:
                stack.appendleft(now+1)
                result.append(now+1)
            else:
                break
        else:
            break

    re_stack.append(num)   
    while True:
        now = re_stack[0]
        if now - 1 == 1:
            if tob_1[2] != tob_2[6]:
                re_stack.appendleft(now-1)
                result.append(now-1)
            else:
                break
        elif now - 1 == 2:
            if tob_2[2] != tob_3[6]:
                re_stack.appendleft(now-1)
                result.append(now-1)
            else:
                break
        elif now - 1 == 3:
            if tob_3[2] != tob_4[6]:
                re_stack.appendleft(now-1)
                result.append(now-1)
            else:
                break
        else:
            break
    
    for n in result:
        
        if abs(num-n) % 2:
            d = dirt * -1
        else:
            d = dirt
            
        if n == 1:
            turn(tob_1,d)
        elif n == 2:
            turn(tob_2,d)
        elif n == 3:
            turn(tob_3,d)
        elif n == 4:
            turn(tob_4,d)


total = 0

if tob_1[0] == 1:
    total += 1

if tob_2[0] == 1:
    total += 2

if tob_3[0] == 1:
    total += 4

if tob_4[0] == 1:
    total += 8

print(total)