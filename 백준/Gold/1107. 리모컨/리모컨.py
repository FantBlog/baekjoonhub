def re2(numbers):
    ln = len(numbers)
    total = 0
    sume = 9999999
    result = 9999999
    if m < 10:
        for idx,num in enumerate(numbers):
            mn = 9
            if num == ' ':
                num = 0
            else:
                num = int(num)

            for err in range(10):
                if abs(num-err) < mn and err not in error:
                    sume = err * 10 ** (ln - idx -1)
                    mn = abs(num-err)
            total += sume
        result = abs(int(numbers) - total) + len(numbers)
    return result

def re3(numbers):
    result = 9999999
    if m < 10:
        su_number = int(numbers)
        while 0 <= su_number:
            err = True
            for number in str(su_number):
                if int(number) in error:  # 고장난 수자 누르면
                    err = False
                    break # 탈출
            
            if err: # 검사하는 수중에 고장난게 하나도 없으면
                result = abs(int(numbers) - su_number) + len(str(su_number))
                break
            su_number -= 1
    return result

def re4(numbers):
    result = 9999999
    if m < 10:
        su_number = int(numbers)
        while su_number < 1000000: # 에이 그래도 백만 안에는 누를수있겠지
            err = True
            for number in str(su_number):
                if int(number) in error: # 고장난 수자 누르면
                    err = False
                    break # 탈출
            
            if err: # 검사하는 수중에 고장난게 하나도 없으면
                result = abs(su_number - int(numbers)) + len(str(su_number))
                break
            su_number += 1
    return result

numbers = input().rstrip('\n') # 보고싶은 채널
m = int(input()) # 고장난 버튼수
if m > 0:
    error = list(map(int,input().split()))
else:
    error = []

result1 = abs(int(numbers) - 100) # 100부터 +-로 가는 거리
result2 = re2(numbers)
result3 = re3(numbers) # 내려갈때
result4 = re4(numbers) # 올라갈때

print(min(result1,result2,result3,result4))