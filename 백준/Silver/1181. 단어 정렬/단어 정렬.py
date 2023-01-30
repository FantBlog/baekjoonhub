T = int(input())
text = set()
for test_case in range(1,T+1):
    text.add(input())
# print(text)

# 길이순으로 정렬
text = sorted(text,key= lambda x:len(x))

# print(text)
temp = list()
result = list()
count = 0
for txt in text:
    if len(temp) == 0:
        # 등록된 단어가 없다면
        temp.append(txt)
        idx = 0
        count += 1
    else:
        # print(f'{temp}, {idx}')
        if len(temp[idx]) == len(txt): 
            # 앞에등록된 단어와 길이가 같다면
            temp.append(txt)
            idx += 1
            count += 1
        else:
            # 길이가 다르면
            result += sorted(temp)
            temp.clear()
            temp.append(txt)
            idx = 0
            count += 1
    if count == len(text):
        result += sorted(temp)
for i in result:
    print(i)