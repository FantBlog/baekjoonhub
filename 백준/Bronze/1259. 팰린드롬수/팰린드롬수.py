text = input()
while text != '0':
    isfel = True
    for i in range(len(text)//2):
        if text[i] != text[-1-i]:
            isfel = False
    if isfel:
        print('yes')
    else:
        print('no')
    text = input()