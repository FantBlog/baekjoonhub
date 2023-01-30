T = int(input())
text = set()
for test_case in range(1,T+1):
    text.add(input())
text = sorted(text,key= lambda x:len(x))
temp = list()
result = list()
count = 0
for txt in text:
    if len(temp) == 0:
        temp.append(txt)
        idx = 0
        count += 1
    else:
        if len(temp[idx]) == len(txt): 
            temp.append(txt)
            idx += 1
            count += 1
        else:
            result += sorted(temp)
            temp.clear()
            temp.append(txt)
            idx = 0
            count += 1
    if count == len(text):
        result += sorted(temp)
for i in result:
    print(i)