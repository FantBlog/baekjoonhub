import sys
input = sys.stdin.readline

def z(size,r,c,count):
    center = size // 2
    if center == 1:
        for x in range(size):
            for y in range(size):
                if x == r and y == c:
                    print(count)
                count += 1
        return 
    area = center ** 2
    if r < center and c < center:
        z(center,r,c,count)
    elif r < center and c >= center:
        z(center,r,c-center,count + area)
    elif r >= center and c < center:
        z(center,r-center,c,count + 2 * area)
    elif r >= center and c >= center:
        z(center,r-center,c-center,count + 3 * area)

n, r, c = map(int,input().split())
size = 2**n
z(size,r,c,0)