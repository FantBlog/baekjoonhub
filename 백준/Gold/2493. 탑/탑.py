n = int(input())
top = list(map(int,input().split()))
result = [0] * n
count = []
while top: # 탑정보가 있다면
    n -= 1 # 인덱스 번호
    count.append((top.pop() , n)) # 탑 높이, 인덱스 
    while top and count and top[-1] > count[-1][0]:
        a = count.pop()
        result[a[1]] = n # 탑 높이가 작은 칸 은 지금 인덱스 저장

print(*result)