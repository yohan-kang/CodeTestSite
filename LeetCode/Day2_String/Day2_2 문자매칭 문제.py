class Solution(object):
    
    # # case 1 뷸필요 요소 많음 
    def isSubsequence(self, s, t):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: bool
    #     """


    #     s_length = len(s)
    #     t_length = len(t)
    #     count = 0
    #     i = 0
    #     j = 0
    #     result = False


    #     if s_length == 0 :
    #         return True

    #     while i != t_length:

    #         if s[j] == t[i]:
    #             j = j+1
    #             count += 1 
    #             if count == s_length:
    #                 result = True
    #                 break
    #         i = i + 1


    #     return result

# case2 불필요요소 제거 
        i = 0
        j = 0


        if len(s) == 0 :
            return True

        while i != len(t):
            if s[j] == t[i]:
                j = j+1
                if j == len(s):
                    return True
            i = i + 1
        return False



# 가장 빠른 작성법   : 
# 1 s를 리스트 요소로 변환하고  
# 2 t요소를 하나씩 확인 하면서 s요소와 매칭이면 
# 3 s요소에 pop(0) 을 한다  

# class Solution(object):
#     def isSubsequence(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         stack = list(s)
#         for ch in t: 
#             if stack and stack[0] == ch : 
#                 stack.pop(0)
#         return stack==[]


# # 이건 추가 예쩨 

# class Solution(object):
#     def isSubsequence(self, s, t):
#         i=j=0
#         if len(s)==0:
#             return True
#         while j<len(t):
#             if s[i]==t[j]:
#                 i+=1
#             if i==len(s):
#                 return True
#             j+=1
#         return False