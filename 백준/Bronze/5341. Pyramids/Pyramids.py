dp = dict()

def fac(n):
    if dp.get(n):
        return dp.get(n)
    
    if n == 1:
        return 1
    
    return fac(n - 1) + n

while True:
    num = int(input())
    if num == 0:
        break
    
    if dp.get(num):
        print(dp[num])
        continue
    
    print(fac(num))