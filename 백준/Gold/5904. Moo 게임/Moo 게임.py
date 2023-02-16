def moo(n):
    count = 0
    while True:
        dp[count + 1] = 2 * dp[count] + count + 4
        if dp[count + 1] > n:
            break
        count += 1
    return count
def find(n,count):
    if n < 4:
        if n == 1:
            print('m')
        else:
            print('o')
        return
    elif dp[count] > n:
        find(n,count-1)
    elif dp[count] < n <= dp[count] + count + 4:
        if n - dp[count] == 1:
            print('m')
            return
        else:
            print('o')
            return
    else:
        find(n - (dp[count] + count + 4), count-1)

dp = {0:3}


n = int(input())
count = moo(n)
find(n, count)