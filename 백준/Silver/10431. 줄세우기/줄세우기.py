for _ in range(int(input())):
    a, *arr = map(int,input().split())
    cnt = 0
    for i in range(19):
        for j in range(19-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                cnt += 1
    print(a,cnt)