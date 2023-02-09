import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    wear_dict = {}
    if n:
        for _ in range(n):
            a,b = input().split()
            wear_dict.setdefault(b,set())
            wear_dict[b].add(a)
        cloths = len(wear_dict)
        total = 0

        for key in wear_dict:
            if total != 0:
                total *= len(wear_dict[key])+1
            else:
                total += len(wear_dict[key])+1
        print(total-1)
    else:
        print(0)