map_x, map_y = map(int, input().split())
x, y = map(int, input().split())
time = int(input())

# time = time % (map_x*map_y)

go_x = (x + time) % (map_x*2)
go_y = (y + time) % (map_y*2)

if go_x > map_x:
    go_x = 2*map_x - go_x
if go_y > map_y:
    go_y = 2*map_y - go_y

print(go_x, go_y)
