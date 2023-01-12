T = int(input())
for test_case in range(1, T + 1):
    a = map(int,list(input().split()))
    max = 0
    for x in a:
        if max < x:
            max =x
    print(f"#{test_case} {max}")