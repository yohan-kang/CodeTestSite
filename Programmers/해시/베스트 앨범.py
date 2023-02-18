# 문제 설명
# 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

# 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
# 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

# 제한사항
# genres[i]는 고유번호가 i인 노래의 장르입니다.
# plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
# genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
# 장르 종류는 100개 미만입니다.
# 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
# 모든 장르는 재생된 횟수가 다릅니다.
# 입출력 예
# classic 장르는 1,450회 재생되었으며, classic 노래는 다음과 같습니다.

# 고유 번호 3: 800회 재생
# 고유 번호 0: 500회 재생
# 고유 번호 2: 150회 재생
# pop 장르는 3,100회 재생되었으며, pop 노래는 다음과 같습니다.

# 고유 번호 4: 2,500회 재생
# 고유 번호 1: 600회 재생
# 따라서 pop 장르의 [4, 1]번 노래를 먼저, classic 장르의 [3, 0]번 노래를 그다음에 수록합니다.

# 장르 별로 가장 많이 재생된 노래를 최대 두 개까지 모아 베스트 앨범을 출시하므로 2번 노래는 수록되지 않습니다.
# ※ 공지 - 2019년 2월 28일 테스트케이스가 추가되었습니다.
# genres	plays	return
# ["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]

def solution(genres, plays):
    answer = []

    dic1 = {} # {'classic': [(0, 500), (2, 150), (3, 800)], 'pop': [(1, 600), (4, 2500)]}
    dic2 = {} # {'classic': 1450, 'pop': 3100}
   
    for i, (g, p) in enumerate(zip(genres, plays)):
        # 0 classic 500
        # 1 pop 600
        # 2 classic 150
        # 3 classic 800
        # 4 pop 2500
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        # k, v
        #  pop 3100
        # classic 1450
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer

# 정답  
# 딕셔너리와 튜플을 잘활용하여 닶을 맟추었다 
def solution(genres, plays):
    answer = []
    total={} #장르별 총 재생횟수 [('pop', 3100), ('classic', 1450)]
    gen_dic={} #장르별 [재생횟수&고유번호]  {'classic': [(500, 0), (150, 2), (800, 3)], 'pop': [(600, 1), (2500, 4)]}
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genres[i] in total.keys():
            total[genres[i]]+=plays[i]
            gen_dic[genres[i]].append((plays[i],i))
        else:
            total[genres[i]]=plays[i]
            gen_dic[genre]=[(play,i)]

        
    total = sorted(total.items(), key=lambda x: x[1], reverse=True)
    
    # print(total)
    # print(gen_dic)
    
    for key in total:
        playlist = gen_dic[key[0]]
        playlist = sorted(playlist, key=lambda x: x[0], reverse=True)
        for i in range(len(playlist)):
            if i==2:
                break
            answer.append(playlist[i][1])
    return answer