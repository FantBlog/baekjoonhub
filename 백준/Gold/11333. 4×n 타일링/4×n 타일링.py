import sys
input = sys.stdin.readline

dp={3:3,6:13}
t = int(input())
for tc in range(t):
    n = int(input())
    if n % 3 != 0:
        print(0)
        continue
    if dp.get(n) != None:
        print(dp[n])
        continue
    for i in range(9,n+4,3):
        if dp.get(i) == None:
            pls = 3
            result = 0
            for j in range(i-3, 2,-3):
                result += dp[j] * pls
                if pls == 3:
                    pls += 1
                else:
                    pls += 2
            result += pls
            dp[i] = result % 1_000_000_007
    print(dp[n])