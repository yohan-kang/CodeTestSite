# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
# 입출력 예
# numbers	return
# [6, 10, 2]	"6210"
# [3, 30, 34, 5, 9]	"9534330"


def solution(numbers):
    numbers = list(map(str, numbers))
    print(numbers) # map 을 이용하여 리스트 안에 숫자들을 문자로 변경 
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
    
# 마지막 에 return ''.join(numbers)만 하면 하나에서 오류가 뜨고 정수화후 문자열변환을 거쳐야 테스트케이스가 모두 통과되는데 이유가 뭘까요?
# 테스트 케이스가 ["0","0","0"] 이라면 정수화 하지 않았을 때 "000"이라는 값이 나오겠죠



# list.sort()와 sorted()는 모두 비교하기 전에 각 리스트 요소에 대해 호출할 함수를 지정하는 key 매개 변수를 가지고 있습니다.
# x * 3 -> 문자열에 3을 곱해주면 해당문자열을 3개 나열하는 것과 같으니

# '333', '303030', '343434', '555', '999'를 key로 넣어주면.

 

# 정렬을 하면 303030 -> 333 -> 343434 -> 555 -> 999가 될 것인데

# reverse=True로 해서 거꾸로 정렬된 결과가 리턴됨.

 

# numbers = ['9', '5', '34', '3', '30']




# 2번 째 방벙 이것도 좋아 보이고 칭찬 많음 

import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer


# 질문 해볼것 작동 원리가 이해가 안감 
# from functools import cmp_to_key

# def compare(x, y):
#     print(x,y)
#     if x+y > y+x:
#     	return -1
#     elif x+y == y+x:
#     	return 0
#     else:
#     	return 1


# l = ['34', '37', '9', '31', '3']
# print( sorted(l, key=cmp_to_key(compare)))

# 37 34
# 9 37
# 31 9
# 31 37
# 31 34
# 3 34
# 3 31
