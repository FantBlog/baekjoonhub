a,b = map(int,input().split())
c = int(input())
b += c
while b>=60:
    if b>=60:
        b -= 60
        a += 1
if a>23:
    a-=24
print(f'{a} {b}')