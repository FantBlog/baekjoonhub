num = int(input())
if num ==1:
    print('1')
else:
    test = (num-2)//6 + 1
    count = 0
    i = 0
    while True:
        i += 1
        count += i
        # print(f'count = {count}   test = {test}    i = {i}')
        if count >= test:
            # print(f'칸수 = {i+1}')
            print(i+1)
            break