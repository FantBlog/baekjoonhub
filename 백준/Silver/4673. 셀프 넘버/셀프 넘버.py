lst = set(range(1,10000))

def selfnumber(i):
    i = str(i)
    rst = int(i)
    for n in i:
        rst += int(n)
    return rst

for i in range(1,10000):
    if selfnumber(i) in lst:
        lst.remove(selfnumber(i))

lst = list(lst)

for i in range(len(lst)):
    print(lst[i])