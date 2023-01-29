fibbo = [0,1]
def fibona(n):
    if len(fibbo) > n:
        return fibbo[n]
    else:
        for i in range(len(fibbo),n+1):
            fibbo.append(fibbo[i-2]+fibbo[i-1])
        return fibbo[n]

print(fibona(int(input())))