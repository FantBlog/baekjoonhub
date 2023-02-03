num, check = map(int, input().split())
tem = list(map(int,input().split()))
start = tem[:check]
save = sum(start)
next = save
for n in range(num - check):
    # print(save, sum(tem[n+1:n+check+1]))
    # if tem[n] < tem[n+check]:
    #     if save < sum(tem[n+1:n+check+1]):
    #         save = sum(tem[n+1:n+check+1])
    next = next-tem[n]+tem[n+check]
    if save < next:
        save = next

print(save)
