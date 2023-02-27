for tc in range(1,1+int(input())):
    N, M, K = map(int,input().split())
    cho = sorted(list(map(int,input().split())))
    for i in range(N):
        cho[i] = cho[i] // M
    
    # print(cho)
    if cho[0] == 0:
        print(f'#{tc} Impossible')
        continue
    bong = 0
    for i in range(1,max(cho)+1):
        bong += K - cho.count(i)
        if bong < 0:
            print(f'#{tc} Impossible')
            break
    else:
        print(f'#{tc} Possible')