
# 문제 설명
# 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
# completion의 길이는 participant의 길이보다 1 작습니다.
# 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
# 참가자 중에는 동명이인이 있을 수 있습니다.
# 입출력 예
# participant	completion	return
# ["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
# ["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
# ["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"





# 이게 왜 안되었을까 알아보기 

def solution(participant, completion):

    dict ={}
    answer = ''
    for i in participant:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
            
    
    for j in completion:
        print(j)
        if j not in dict:
            answer = j
            break
    return answer




# vest 정답
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


# 진짜 해시함수 사용 
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer


#  정렬후 검색 이것도 나쁘지 않은 접근 
def solution(participant, completion):
    # 1. 두 list를 sorting한다
    participant.sort()
    completion.sort()

    # 2. completeion list의 len만큼 participant를 찾아서 없는 사람을 찾는다
    for i in range(len(completion)):
        if(participant[i] != completion[i]):
            return participant[i]

    # 3. 전부 다 돌아도 없을 경우에는 마지막 주자가 완주하지 못한 선수이다.
    return participant[len(participant)-1]
