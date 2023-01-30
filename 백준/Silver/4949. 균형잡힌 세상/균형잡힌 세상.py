import sys
while True:
    text = input()
    if text == '.':
        break
    balance = True
    stack = list()
    for t in text:
        if t == '.':
            break
        if t in ['(','[']:
            stack.append(t)
        elif t in [')',']']:
            if len(stack) != 0:
                last = stack.pop()
                if last == '(' and t != ')':
                    balance = False
                    break
                if last == '[' and t != ']':
                    balance = False
                    break
            else:
                balance = False
                break
    if len(stack) != 0:
        balance = False
    if balance:
        print('yes')
    else:
        print('no')