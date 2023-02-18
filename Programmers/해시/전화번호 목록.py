# ''문제 설명
# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
# 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

# 구조대 : 119
# 박준영 : 97 674 223
# 지영석 : 11 9552 4421
# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# phone_book의 길이는 1 이상 1,000,000 이하입니다.
# 각 전화번호의 길이는 1 이상 20 이하입니다.
# 같은 전화번호가 중복해서 들어있지 않습니다.
# 입출력 예제
# phone_book	return
# ["119", "97674223", "1195524421"]	false
# ["123","456","789"]	true
# ["12","123","1235","567","88"]	false


# 내가 한거  : 하나씩 순차적으로 잘라서 비교하는 방식  : 몇개는 타임 오버가 나오며 실패 부분도 있음 
def solution(phone_book):
    answer = True
    check = []
    
    for i in range(0,len(phone_book)-1):
        for j in range(i+1,len(phone_book)):
            if len(phone_book[i]) < len(phone_book[j]):
                check = phone_book[j]
                check = check[:len(phone_book[i])]
                # print("phone_book[j]:{} ,check:{} ,phone_book[i]:{}".format(phone_book[j],check,phone_book[i]))
                if int(phone_book[i])==int(check):
                    answer = False
                    return answer
    return answer


def solution(phone_book):
    answer = True
    check = []
    # 정렬을 왜 했는지 아는지가 중요하다 
    # string을 그냥 정렬하면 앞의 글자 순서대로 정렬
    phone_book.sort()

    if len(phone_book) < 2:
        return answer

    for i in range(0,len(phone_book)-1):
        # 원래는 아래 주석처리한 부분으로도 가능하지만 
        # 119  213119 이런 경우를 생각해서 예외 처리를 추가함  
        if len(phone_book[i]) < len(phone_book[i+1]):
            check = phone_book[i+1]
            check = check[:len(phone_book[i])]
            if int(phone_book[i])==int(check):
                answer = False
                return answer

        # if phone_book[i] in phone_book[i+1]:
        #     answer = False
        #     return answer
    return answer



# 제일 좋다고 칭찬이 많은 코드 
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

# 해쉬 정석으로 푼 문제 
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer