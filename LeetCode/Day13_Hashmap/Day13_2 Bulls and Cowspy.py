# 숫자 야구 게임

# Example 1:

# Input: secret = "1807", guess = "7810"
# Output: "1A3B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1807"
#   |
# "7810"
# Example 2:

# Input: secret = "1123", guess = "0111"
# Output: "1A1B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1123"        "1123"
#   |      or     |
# "0111"        "0111"
# Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.





# case 1 n제곱이면서 1123 , 0111 경우 ball을 측정 못해 오류가 있다 
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """   
        strike = 0
        boll = 0

        for i in range(0,len(secret)) :
            
            for j in range(0,len(guess)):

                if secret[i] == guess[j] and i == j:
                    strike +=1
                    break
                if i != j and secret[i] == guess[j]:
                    boll += 1
        result = ("{}A{}B".format(strike,boll))
        return result



# 딕셔너리에 값 넣으면서 하나씩 체크하면서 제거 하기 
# case2
# "1123", guess = "0111"



#         # 1  0 ,1
#         # 2  2
#         # 3  3

#         # 0, 0 
#         # 1 1,2,3
        
#         # 0스킵 , 1 1 스트라이크 , 지우기 , (1,0) (1,2) 볼 , 지우기 
        
#         strike = 0
#         boll = 0
#         dict = {}
#         lst =[]

#         for i in range(0,len(secret)):
#             if secret[i] in dict:
#                 dict[secret[i]].append(i)
#             else:
#                 dict[secret[i]] = [i] 
     
# # del dic1['박한지']


#         for i in range(0,len(guess)):
#             if guess[i] in dict:
#                 for j in range((0,len(guess[i]))
#                     if guess[i][j] in dict[i] :







#        # case 1   
#         strike = 0
#         boll = 0
# # 딕셔너리에 값 넣으면서 하나씩 체크하면서 제거 하기 


#         for i in range(0,len(secret)) :
            
#             for j in range(0,len(guess)):

#                 if secret[i] == guess[j] and i == j:
#                     strike +=1
#                     break
#                 if i != j and secret[i] == guess[j]:
#                     boll += 1
#         result = ("{}A{}B".format(strike,boll))
#         return result



# 빠른 정답??? 
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull=0
        for i in range(len(secret)):
            bull += int(secret[i] == guess[i])
        
        cows=0
        for c in set(secret):
            cows += min(secret.count(c), guess.count(c))
        
        return str(bull)+"A"+str(cows-bull)+"B"

# 정답 

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        x = y = 0
        d = defaultdict(int)
        length = len(secret)
        """
        secret = '1123'
        guess = '0111'
        황소를 제외한 숫자의 개수를 d에 저장한다.
        
        print(d) ->
        defaultdict(<class 'int'>, {'1': 1, '2': 1, '3': 1})

		"""
        for i in range(length):
            if secret[i] == guess[i]:
                x += 1  # 황소 카운트
                continue
            else:
                d[secret[i]] += 1


        for i in range(length):
            if guess[i] not in d or secret[i] == guess[i]:
                continue
            if d[guess[i]] >= 1:
                d[guess[i]] -= 1
                y += 1

        return str(x) + 'A' + str(y) + 'B'

# 조금 더 빠른거?? 
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        correct=0
        data1={}
        data2={}
        for i in range (len(guess)):
            if (secret[i]==guess[i]):
                correct+=1
                continue
                
            if secret[i] not in data1:
                data1[secret[i]]=1
            else:
                data1[secret[i]]+=1
            if guess[i] not in data2:
                data2[guess[i]]=1
            else:
                data2[guess[i]]+=1
        
        incorrect=0
        for i in data1.keys():
            if i in data2:
                if data2[i]>=data1[i]:
                    incorrect+=data1[i]
                else :
                    incorrect+=data2[i]
        i    
        s1=str(correct)
        s2=str(incorrect)
        ans =s1+'A'+s2+'B'
        return ans 