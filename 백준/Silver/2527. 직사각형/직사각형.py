for _ in range(4):
    a,b,c,d,e,f,g,h = map(int,input().split())
    if c<e or d<f or h<b or g<a:
        print('d')
    elif (a,b)==(g,h) or (a,d)==(g,f) or (c,b)==(e,h) or (c,d)==(e,f):
        print('c')
    elif c == e or d == f or a == g or b == h:
        print('b')
    else:
        print('a')