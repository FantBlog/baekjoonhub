T = int(input())
lt = list(map(int,input().split()))
lt = sorted(lt)
if len(lt) == 1:
    print(lt[0]**2)
else:
    print(lt[0] * lt[-1])