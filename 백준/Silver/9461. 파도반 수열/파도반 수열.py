pado = {-1:1,0:0,1:1,2:1,3:1,4:2,5:2,6:3,7:4,8:5,9:7,10:9}

t = int(input())
for _ in range(t):
    n = int(input())
    if pado.get(n) == None:
        for i in range(2,n+1):
            if pado.get(i) == None:
                pado[i] = pado[i-1] + pado[i-5]
        print(pado[n])
    else:
        print(pado[n])