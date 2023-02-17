def solve(i):
    global mx
    if i == n: # 마지막달걀 치고나서
        cnt = 0
        for x in s:
            if x <= 0:
                cnt+=1
        if cnt > mx:
            mx = cnt
        return
    

    if s[i] <= 0: # 들려고했더니 깨져있음
        solve(i+1)

    else:
        tr = True
        for j in range(0,n):
            if i != j and s[j] > 0: # 본인아니고, 깰놈이 살아있음
                tr = False
                s[i] -= w[j]
                s[j] -= w[i]
                solve(i+1)
                s[i] += w[j]
                s[j] += w[i]
        if tr: # 아무것도 못때렸어
            solve(i+1)

n = int(input())
s = []
w = []
for _ in range(n):
    a,b = map(int,input().split())
    s.append(a)
    w.append(b)
mx = 0
solve(0)
print(mx)