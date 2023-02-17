def solve(i,moem,jaem, sajen):
    if i == L:
        temp = ''.join(sorted(vis))
        if temp not in result:
            mo_cnt = ja_cnt = 0
            for txt in temp:
                if txt in ['a','e','i','o','u']:
                    mo_cnt += 1
                else:
                    ja_cnt += 1
            if mo_cnt > 0 and ja_cnt > 1:
                result.add(temp)
        return

    for j in range(C):
        if j >= sajen and can[j] not in vis:
            vis.add(can[j])

            solve(i+1,moem,jaem,j)
            
            vis.remove(can[j])



L, C = map(int,input().split())
can = sorted(list(input().split()))

vis = set()
result = set()

solve(0,0,0, 0)

print(*sorted(result),sep='\n')