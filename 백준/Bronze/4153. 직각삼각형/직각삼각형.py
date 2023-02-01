text = list(map(int,input().split()))
while True:
    if max(text) == 0:
        break
    text = sorted(text)
    if text[0]**2 + text[1]**2 == text[2]**2:
        print('right')
    else:
        print('wrong')
    text = list(map(int,input().split()))