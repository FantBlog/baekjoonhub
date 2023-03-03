def cul(a,center,b):
    if center == '+':
        return a + b
    elif center == '-':
        return a - b
    elif center == '*':
        return a * b

def cal(string):
    stack = []
    
    for ch in string:
        if ch.isdecimal():
            if stack and not stack[-1].isdecimal() and stack[-1] != '(':
                center = stack.pop()
                a = stack.pop()
                stack.append(cul(a,center,int(ch)))
                
            else:
                stack.append(int(ch))
            
        elif ch == ')':

            a = stack.pop()
            stack.pop() # '('
            stack.append(a)

            if len(stack) > 2:
                b = stack.pop()
                c = stack.pop()
                a = stack.pop()
                stack.append(cul(a,c,b))

        
        else:
            stack.append(ch)

    if len(stack) > 2:
        b = stack.pop()
        c = stack.pop()
        a = stack.pop()
        stack.append(cul(a,c,b))

    return stack[0]

N = int(input()) # 수식의 길이 항상 홀수
M = N // 2 # 연산자 개수
text = list(input())

mx = cal(text)
for i in range(1<<M):
    for j in range(M-1):
        if i & (1<<j) and i & (1<<(j+1)):
            break
    else:
        temp = text[:]
        
        for j in range(M-1,-1,-1):
            if i & (1<<j):
                temp[j*2:j*2+3] = ['('] + text[j*2:j*2+3] + [')']

        if mx < cal(temp):
            mx = cal(temp)
print(mx)
