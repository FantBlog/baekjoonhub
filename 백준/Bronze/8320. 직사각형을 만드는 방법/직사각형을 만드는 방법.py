N = int(input())
total = N
for i in range(2,N):
    if N//i - i + 1 >= 1:
        total += N//i - i + 1
    else:
        break
print(total)