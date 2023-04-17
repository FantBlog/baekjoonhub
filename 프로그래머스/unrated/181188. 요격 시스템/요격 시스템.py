def solution(targets):
    answer = 1
    targets.sort()
    end = 100_000_001
    for target in targets:
        # print(target, end)
        if end <= target[0]:
            answer += 1
            end = target[1]
            # print('count')
        else:
            if end > target[1]:
                end = target[1]
        # print(target, end)
    
    
    return answer