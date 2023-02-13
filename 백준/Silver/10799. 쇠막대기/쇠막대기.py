from collections import deque
lazor = deque()
text = input()
count = 0
cut = False
for txt in text:
    if txt == ')' and cut:
        lazor.pop()
        count += len(lazor)
        cut = False
    elif txt == ')':
        lazor.pop()
        count += 1
    else:
        lazor.append(txt)
        cut = True
print(count)