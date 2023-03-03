size = 100
arr = [[0]*size for _ in range(size)]
for _ in range(int(input())):
    R, C = map(int,input().split())
    for r in range(R,R+10):
        for c in range(C,C+10):
            if not(0 <= r < size and 0 <= c < size):
                continue
            arr[r][c] = 1
dd = (
    (0,1),
    (0,-1),
    (1,0),
    (-1,0)
)
cnt = 0
for r in range(size):
    for c in range(size):
        for dr, dc in dd:
            if arr[r][c] == 1:
                if not(0 <= r + dr < size and 0 <= c + dc < size):
                    cnt += 1
                    continue
                if arr[r+dr][c+dc] == 0:
                    cnt += 1
print(cnt)