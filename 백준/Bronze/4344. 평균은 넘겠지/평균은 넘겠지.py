T = int(input())
for test_case in range(T):
    lst = list(map(int,input().split()))
    avr = sum(lst[1:])/lst[0]
    jal = 0
    for i in range(1,lst[0]+1):
        if lst[i] > avr:
            jal += 1
    print(f'{jal*100/lst[0]:.3f}%')