t = int(input())
text = input()
total = 0
for i in range(t):
    total += (ord(text[i])-96)*(31**i)
print(total)