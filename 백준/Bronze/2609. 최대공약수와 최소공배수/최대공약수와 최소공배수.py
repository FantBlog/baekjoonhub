a,b = map(int,input().split())
a1 = a
b1 = b
nam = 1
while nam != 0:
    if a1 > b1:
        a1 = a1 % b1
        nam = a1
    else:
        b1 = b1 % a1
        nam = b1
print(max(a1,b1))
print(a*b//max(a1,b1))