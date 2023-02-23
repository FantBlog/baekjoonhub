import sys
input = sys.stdin.readline
A, B = map(int,input().split())
L , R = 0 , 0
while A != 1 or B != 1:
    if A > B:
        L += 1
        A -= B
    else:
        R += 1
        B -= A
print(L,R)