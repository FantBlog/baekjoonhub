a = int(input())
b = int(input())
c = int(input())
r = a*b*c
l = [0]*10
for i in str(r):
    l[int(i)] += 1
for i in l:
    print(i)