a,b,c = map(int,input().split())
if (c-a) % (a-b):
    print(((c-a) // (a-b) +1)+1)
else:
    print((c-a) // (a-b) + 1)