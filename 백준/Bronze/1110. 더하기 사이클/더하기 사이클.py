t = int(input())
a = t
c = 0
while 1:
    i = a//10
    o = a%10
    p = i + o
    c += 1
    a = o*10+p%10
    if a == t:
        break
print(c)