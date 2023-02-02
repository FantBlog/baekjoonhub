t = int(input())
for test_case in range(t):
    minsu = list(map(int,input().split()))
    cersu = list(map(int,input().split()))
    count_minsu = [0]*4
    count_cersu = [0]*4
    for i in minsu[1:]:
        count_minsu[i-1] += 1
    for i in cersu[1:]:
        count_cersu[i-1] += 1
    # print(count_minsu,count_cersu)

    if count_minsu[3] > count_cersu[3]:
        print('A')
        continue
    elif count_minsu[3] < count_cersu[3]:
        print('B')
        continue
    elif count_minsu[2] > count_cersu[2]:
        print('A')
        continue
    elif count_minsu[2] < count_cersu[2]:
        print('B')
        continue
    elif count_minsu[1] > count_cersu[1]:
        print('A')
        continue
    elif count_minsu[1] < count_cersu[1]:
        print('B')
        continue
    elif count_minsu[0] > count_cersu[0]:
        print('A')
        continue
    else:
        print('D')