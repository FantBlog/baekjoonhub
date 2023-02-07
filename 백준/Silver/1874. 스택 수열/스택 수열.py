from collections import deque
n = int(input())
st = deque()
count = 1
result = ''
for _ in range(n):
    a = int(input())
    if count < a+1:
        for _ in range(a-count+1):
            st.append(count)
            count += 1
            result += result.join('+')
        st.pop()
        result += result.join('-')
    else:
        if st.pop() == a:
            result += result.join('-')
        else:
            print('NO')
            exit()
print(*result,sep='\n')