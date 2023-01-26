value = int(input())
total = 0
count = 0
a = b = 1
for i in range(1,value+1):
    total += i
    if value <=total:
        timing = value - (total - i)
        if timing == 1:
            if i % 2:
                a = i
            else:
                b = i
        else:
            if i % 2:
                a = i - (timing-1)
                b = timing
            else:
                a = timing
                b = i - (timing-1)
            pass
        print(f'{a}/{b}')
        break