import sys
input = sys.stdin.readline
t = int(input())
text = []

for _ in range(t):
    text.append(input().rstrip('\n'))

result = text[:]
find = {}
for num in text:
    basu = len(num) - 1
    count = 0
    for i in num:
        find.setdefault(i,0)
        find[i] += 10 ** (basu - count)
        count += 1

al = {}
count = 9
for i in range(len(find)):
    mx = max(find.items(),key=lambda x : x[1])
    al[mx[0]] = count
    count -= 1
    find[mx[0]] = 0

total = 0
for string in result:
    temp = 0
    for i in string:
        temp *= 10
        temp += al[i]
    total += temp
print(total)