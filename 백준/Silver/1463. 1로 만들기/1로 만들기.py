num_dict = {1:0}
num = int(input())
for n in range(2,num+1):
    if n % 3 == 0 and n % 2 == 0:
        num_dict[n] = min(num_dict.get(n // 3), num_dict.get(n // 2), num_dict.get(n - 1)) + 1
    elif n % 3 == 0:
        num_dict[n] = min(num_dict.get(n // 3), num_dict.get(n - 1)) + 1
    elif n % 2 == 0:
        num_dict[n] = min(num_dict.get(n // 2), num_dict.get(n - 1)) + 1
    else:
        num_dict[n] = num_dict.get(n - 1) + 1

print(num_dict.get(num))