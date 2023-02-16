def lotto(i,jun):
    if i == 7:
        print(*lottos)
        return
    
    for j in range(i,S[0]+1):
        if S[j] > jun and S[j] not in visi:
            lottos.append(S[j])
            visi.append(S[j])
            lotto(i+1 , S[j])
            lottos.pop()
            visi.pop()

while True:
    S = list(map(int,input().split()))

    if S[0] == 0:
        exit()
    
    visi = []
    lottos = []
    lotto(1,0)
    print()