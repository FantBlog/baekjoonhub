a,b = map(int,input().split())
b += 15
a -= 1
if b>=60:
    b -= 60
    a += 1
if a<0:
    a+=24
print(f'{a} {b}')