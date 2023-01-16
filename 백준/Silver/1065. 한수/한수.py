def hansu(a):
    cha = 0
    bol = True
    temp = str(a)
    if len(temp)>1:
        for i in range(len(temp)-1):
            if i == 0:
                cha = int(temp[i]) - int(temp[i+1])
            else:
                if int(temp[i]) - int(temp[i+1]) != cha:
                    bol = False
    else:
        return bol
    return bol
t = int(input())
rst = 0
for i in range(1,t+1):
    rst += hansu(i)
print(rst)