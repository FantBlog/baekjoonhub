tr = int(input())
for i in range(tr):
    ox = input()
    total_score = 0
    score = 0
    for j in range(len(ox)):
        if ox[j] == 'O':
            score += 1
            total_score +=score
        else:
            score = 0
    print(total_score)