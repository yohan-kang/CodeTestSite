# 영어 대문자로만 구성된 문자열이 주어지면 해당 문자열에 대해 최대 k 개의 연산을 수행 할 수 있습니다. 
# 한 번의 작업에서 문자열의 문자를 선택하고 다른 대문자 영어 문자로 변경할 수 있습니다. 
# 위의 작업을 수행 한 후 얻을 수 있는 모든 반복 문자를 포함하는 가장 긴 하위 문자열의 길이를 찾습니다.class Solution(object):


# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.


# 투 포인터  left right 두고 풀기 



# 실패함 
# "LRIJHRABBJGQAOLIKRLHDRIGERENNMJSDSSMESSTR" 이런경우 S를 앞에서 끊어서 6이아니라 5가나와서 실패 
# class Solution(object):
#     def characterReplacement(self, s, k):
#         """
#         :type s: str
#         :type k: int
#         :rtype: int
#         """
#         life = k 
#         lenth = 0 
#         abc = set(s)
#         word = s
#         count = 0
#         len_max = 0

#         print(abc)

#         for i in abc:
#             count = 0
#             for j in range(0,len(word)):
#                 # print("i:{} , j:{}".format(i,j))
#                 if word[j] == i :
#                     count +=1
#                     if len_max < count :
#                         len_max = count

#                 else :
#                     if life != 0 : 
#                         count +=1
#                         life = life-1
#                         # print("i:{},word[j]:{} , count :{}".format(i,word[j],count))
#                         if len_max < count :
#                             len_max = count
#                     else:
#                         count = 0
#                         life = k
#             # print("i:{} , len_max :{}".format(i,len_max))
#         return len_max










class Solution:
    def characterReplacement(self, s, k):
        max_freq = res = 0
        count = collections.Counter()

        left = right = 0

        while right < len(s):
            count[s[right]] += 1
            max_freq = max(max_freq, count[s[right]])

            if res < max_freq + k:
                res += 1
            else:
                count[s[right - res]] -= 1
                left += 1

            right += 1
        return res

class Solution(object):
    def characterReplacement(self, s, k):
        ans = 0
        f = {}
        for i in s:
            f[i] = 0


        maxfreq=i=j=0
        while(j<len(s)):
            f[s[j]]+=1
            maxfreq = max(maxfreq,f[s[j]])
            window = (j-i+1)
            if(window-maxfreq <= k):
                ans = max(j-i+1,ans)
                j+=1
            else:
                f[s[i]]-=1
                i+=1
                j+=1
        
        return ans