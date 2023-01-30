number = int(input())
def soinsu(number):
    if number == 1:
        return 
    for i in range(2,number+1):
        if number % i == 0:
            print(i)
            soinsu(number // i)
            break
    return
soinsu(number)