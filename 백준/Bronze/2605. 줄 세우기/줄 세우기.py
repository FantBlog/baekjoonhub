T = int(input())
num_list = list(map(int,input().split()))
result = []
for i in range(T):
    result.insert(len(result)-num_list[i],i+1)
for i in range(T):
    print(result[i],end=' ')