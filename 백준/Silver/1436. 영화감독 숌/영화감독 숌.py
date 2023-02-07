dv = '666'
n = int(input())
count = i = 0
while True:
    i += 1
    if dv in str(i):
        count += 1
    if count == n:
        print(i)
        break