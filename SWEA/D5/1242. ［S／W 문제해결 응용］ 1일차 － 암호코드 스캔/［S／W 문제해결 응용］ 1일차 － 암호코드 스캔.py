from collections import deque
base = ([2,1,1],
        [2,2,1],
        [1,2,2],
        [4,1,1],
        [1,3,2],
        [2,3,1],
        [1,1,4],
        [3,1,2],
        [2,1,3],
        [1,1,2])

def new_decode(text):
    global total
    # text = bin(int(text,16))[2:].rstrip('0')
    num_list = [0,0,0]
    num_idx = 2
    
    result = deque()
    
    while len(text) % 56: # 56의 배수만큼 0 추가
        text = '0' + text
        
    # if tc == 13:
    #     브레이크 = 0
        
    for c in range(len(text)-1,-1,-1): # 뒤에서부터
        if num_idx < 3:
            num_list[num_idx] += 1
        
        if text[c] != text[c-1]: # 바뀔때마다
            num_idx -= 1 # 앞으로
            
        if num_idx < 0:
            mn = min(num_list)

            for i in range(3):
                num_list[i] //= mn
                
            result.appendleft(base.index(num_list))
            
            if len(result) == 8:
                break
            
            num_idx = 3
            num_list = [0,0,0]
    
    
    
    # if use.get(tuple(result)) == r - 1:
    #     use[tuple(result)] = r
        
    # if use.get(tuple(result)) == None:
    if tuple(result) not in use:
    # else:
        is_code = 0
        for i in range(8):
            if i % 2:
                is_code += result[i]
            else:
                is_code += result[i] * 3
        
        if not is_code % 10:
            total += sum(result)
            use.add(tuple(result))
            # use[tuple(result)] = r
        
    return text[:c].rstrip('0')


t = int(input())
for tc in range(1,t+1):
    R, C = map(int,input().split())
    numbers = list(set(input() for _ in range(R)))
    RR = len(numbers)
    total = 0
    use = set()
    
    for r in range(RR):
        now = bin(int(numbers[r],16))[2:].rstrip('0')
        while now:
            now = new_decode(now)
    print(f'#{tc} {total}')