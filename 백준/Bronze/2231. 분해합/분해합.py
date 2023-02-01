t = int(input())
result = 0
for i in range(t):
    total = 0
    for j in str(i):
        total += int(j)
    total += i
    if total == t:
        result = i
        break
print(result)