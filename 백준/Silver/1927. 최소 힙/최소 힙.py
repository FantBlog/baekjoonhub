import sys
input = sys.stdin.readline

def in_hip(hip,num):
    hip.append(num)
    mom_idx = (len(hip)-1) // 2
    son_idx = (len(hip)-1)
    while son_idx >= 2:
        if hip[mom_idx] > hip [son_idx]:
            hip[mom_idx] , hip [son_idx] = hip[son_idx] , hip [mom_idx]
        else:
            break
        son_idx = mom_idx
        mom_idx //= 2
    return hip

def out_hip(hip):
    if len(hip) == 1:
        print(0)
        return hip
    print(hip.pop(1))
    if len(hip)== 1:
        return hip
    hip.insert(1,hip.pop(-1))
    idx = 1
    son = idx * 2
    while (len(hip)-1) > son:
        if hip[son] < hip[son+1] and hip[son] < hip[idx]:
            hip[idx] , hip[son] = hip[son] , hip[idx]
            idx = son
        elif hip[son+1] < hip[idx]:
            hip[idx] , hip[son+1] = hip[son+1] , hip[idx]
            idx = son + 1
        else:
            break
        son = idx * 2

    if (len(hip)-1) == son:
        if hip[son] < hip[idx]:
            hip[idx] , hip[son] = hip[son] , hip[idx]
    return hip

n = int(input())
hip = [0]
for _ in range(n):
    a = int(input())
    if a:
        hip = in_hip(hip,a)
    else:
        hip = out_hip(hip)