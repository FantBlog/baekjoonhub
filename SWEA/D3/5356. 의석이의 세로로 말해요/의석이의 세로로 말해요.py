size = 5
for tc in range(1,int(input())+1):
    text = [list(input()) for _ in range(size)]


    print(f'#{tc} ',end='')
    for r in range(max(len(text[i]) for i in range(size))):
        for c in range(size):
            try:
                print(text[c][r],end='')
            except:
                pass
    print()