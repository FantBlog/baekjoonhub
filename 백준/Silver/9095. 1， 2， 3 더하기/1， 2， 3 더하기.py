t = int(input())
fire = [1,2,4]
for _ in range(t):
    n = int(input())
    for i in range(3,n):
        if len(fire) <= i:
            fire.append(fire[i-1]+fire[i-2]+fire[i-3])
    print(fire[n-1])