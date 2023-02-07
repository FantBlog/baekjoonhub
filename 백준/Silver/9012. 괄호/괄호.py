from collections import deque
import sys
t = int(input())
for _ in range(t):
    text = list(sys.stdin.readline().rstrip('\n'))
    st = deque()
    bl = True
    for i in range(len(text)):
        if text[i] == '(':
            st.append(1)
        elif text[i] == ')':
            try:
                st.pop()
            except:
                bl = False
                break
    if len(st):
        bl = False
    if bl:
        print('YES')
    else:
        print('NO')