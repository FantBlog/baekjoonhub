t = int(input())
count = 0
for test_case in range(1,t+1):
    text = input()
    used_word = set()
    for i in range(len(text)): 
        try: # 첫단어 스킵을 이렇게 잡을수 있지않을까
            if text[i-1] != text[i]: # 앞 문자랑 다른데
                if text[i] in used_word: # 쓴 문자다?
                    # print(f'나갈놈 {text[i]}')
                    break # 넌 나가라
        except:
            pass
        used_word.add(text[i]) # 나중에 쓴 문자 넣어
        if i + 1 == len(text):
            count += 1 # 견뎠으면 점수주기
        
    
print(count)