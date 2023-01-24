text = input()
result = ''

for i in text:

    if ord(i) == 32:
        result += i
        continue

    if 122 >= ord(i) >= 97 or 90 >= ord(i) >= 65:
        if  ord(i) >= 110:
            result += (chr(ord(i)-13))
        elif 90 >= ord(i) >= 78:
            result += (chr(ord(i)-13))
        else:
            result += (chr(ord(i)+13))
    else:
        result += i

print(f'{result}')