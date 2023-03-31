import sys
from heapq import heappush

def input(): return sys.stdin.readline().rstrip()

def cp(a, b, c):
    v1 = [b[0] - a[0], b[1] - a[1]]
    v2 = [c[0] - b[0], c[1] - b[1]]
    return v1[0] * v2[1] - v1[1] * v2[0]

def x_case(p1, p2, p3, p4): return max(p1[0], p2[0]) < min(p3[0], p4[0]) or max(p3[0], p4[0]) < min(p1[0], p2[0])
def y_case(p1, p2, p3, p4): return max(p1[1], p2[1]) < min(p3[1], p4[1]) or max(p3[1], p4[1]) < min(p1[1], p2[1])

N = int(input())
Lines = list()

for i in range(N):
    a, b, c, d = map(int, input().split())
    if c < a :
        a,b,c,d = c,d,a,b
    heappush(Lines,(a, (a,b),(c,d)))

ans = 0

L_Point = 0
R_Point = 1

while R_Point != N:
    _, p1, p2 = Lines[L_Point]
    _, p3, p4 = Lines[R_Point]

    if x_case(p1, p2, p3, p4) or y_case(p1, p2, p3, p4):
        if x_case(p1, p2, p3, p4): # 포인터 초기화
            L_Point += 1
            R_Point = L_Point + 1
        else: # 다음거 탐색
            R_Point += 1

    else:
        # 외적의 특징을 이용해서 교점의 존재 유무를 찾음
        case1 = cp(p1, p2, p3) * cp(p1, p2, p4)
        case2 = cp(p3, p4, p1) * cp(p3, p4, p2)

        if (case1 <= 0 and case2 <= 0) and not (case1 == 0 and case2 == 0):
            ans = 1
            break

        if R_Point < N: # 아직 탐색 가능
            R_Point += 1
        else: # 끝까지 갔으면 왼쪽 포인터 이동
            L_Point += 1
            R_Point = L_Point + 1

print(ans)
