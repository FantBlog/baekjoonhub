text = input()
result = 0
count = 0
ln = len(text)
for i in range(ln):

    if count > 0:
        count -= 1
        continue

    if text[i] == 'c':
        if (ln-i-1) and text[i+1] in ['-','=']:
            count = 1
            result += 1
            continue

    if text[i] == 'd':
        if (ln-i-1) and text[i+1] == '-':
            count = 1
            result += 1
            continue

        elif (ln-i-2) and text[i:i+3] == 'dz=':
            count = 2
            result += 1
            continue

    if text[i] == 'l':
        if (ln-i-1) and text[i+1] == 'j':
            count = 1
            result += 1
            continue

    if text[i] == 'n':
        if (ln-i-1) and text[i+1] == 'j':
            count = 1
            result += 1
            continue

    if text[i] == 's':
        if (ln-i-1) and text[i+1] == '=':
            count = 1
            result += 1
            continue

    if text[i] == 'z':
        if (ln-i-1) and text[i+1] == '=':
            count = 1
            result += 1
            continue
    result +=1
print(result)