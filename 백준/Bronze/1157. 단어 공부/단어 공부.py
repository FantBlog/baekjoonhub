text = input().upper()
dct = dict()
for i in text:
    dct.setdefault(i,0)
    dct[i] += 1

dct = sorted(dct.items(),key=lambda x:x[1],reverse=True)

# print(dct)
# print(dct[0][1],dct[1][1])

if len(dct) == 1:
    print(dct[0][0])
elif dct[0][1] == dct[1][1]:
    print('?')
else:
    print(dct[0][0])