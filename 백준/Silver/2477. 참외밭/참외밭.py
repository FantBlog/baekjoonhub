k = int(input())
hori = []
vert = []
record_hori = []
record_vert = []
for _ in range(6):
    direct, width = map(int,input().split())
    if direct > 2:
        vert.append(width)
        record_vert.append((direct,width))
    else:
        hori.append(width)
        record_hori.append((direct,width))
    
v = max(vert)
h = max(hori)

for idx, val in enumerate(vert):
    if val == v:
        v_i = idx
        break
for idx, val in enumerate(hori):
    if val == h:
        h_i = idx
        break

for i in record_vert:
    if i[1] == v:
        z = i[0]
        break
for i in record_hori:
    if i[1] == h:
        x = i[0]
        break
if (z+x) % 2:
    result = (v * h - vert[(v_i + 1)%3] * hori[h_i - 1])
    print(result*k)
else:
    result = (v * h - vert[v_i - 1] * hori[(h_i + 1)%3])
    print(result*k)