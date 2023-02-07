import sys
input = sys.stdin.readline
n = int(input())
cards = list(map(int,input().split()))
m = int(input())
finds = list(map(int,input().split()))
dic_cards = dict()
for i in cards:
    dic_cards.setdefault(i,0)
    dic_cards[i] += 1
for num in finds:
    dic_cards.setdefault(num,0)
    print(dic_cards.get(num),end=' ')