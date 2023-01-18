S = input()

Alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
        'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
        'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
result = [-1] * len(Alph)

count = 0
for i in S:
    idx = Alph.index(i)
    if result[idx] == -1:
        result[idx] = count
    count += 1

for i in result:
    print(i, end=' ')