T = int(input())
for i in range(T):
    a,b,c = map(int,input().split())
    chng=c%a
    ho = c//a + 1
    if chng == 0:
        ho -= 1
        chng = a
    print((chng * 100)+ ho)