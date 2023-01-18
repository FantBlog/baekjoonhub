t = int(input())
for test_case in range(t):
    text, print_text = input().split()
    for i in print_text:
        print(i * int(text) , end='')
    print()