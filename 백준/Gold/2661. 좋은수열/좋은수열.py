def is_good():
    for i in range(1,len(result)):
        for j in range(1,1+min(i,len(result)-i)):
            if result[i-j:i] == result[i:i+j]:
                return True
    return False

def good(num):
    if is_good():
        return
    if num == N:
        print(*result,sep='')
        exit()
    for i in range(1,4):    
        result.append(i)
        good(num+1)
        result.pop()
    
N = int(input())
result = []
good(0)