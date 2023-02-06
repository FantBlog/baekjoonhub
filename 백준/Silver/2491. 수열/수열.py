import sys
n  = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
o = 0
mx = 1
p = up_count = dn_count = 1
for _ in range(n-1):

    if lst[o] <= lst[p]:
        up_count += 1
    else:
        up_count = 1
    if lst[o] >= lst[p]:
        dn_count += 1
    else:
        dn_count = 1
    p += 1
    o += 1

    if mx < up_count:
        mx = up_count
    if mx < dn_count:
        mx = dn_count
print(mx)