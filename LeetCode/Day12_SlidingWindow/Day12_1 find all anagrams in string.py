

# 문자열을 주어지고 p에서 주어진 문자에 순서에 상관없이 조합해서 문장이 만들어지면 그 시적점을 반환 한다 
# 2 예시   0 ab 1 ba 2 ab 3 는 불가능 그래서 0 ,1,2 





# Example 1:
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

# Example 2:
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".






# 정석 답인것 같음 
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        if len(p) > len(s): return []
        
        pCount, sCount = {}, {}

        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)

        res = [0] if sCount == pCount else []
        l = 0

        for r in range(len(p), len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)     
            sCount[s[l]] -= 1

            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1

            if sCount == pCount:
                res.append(l)
        
        return res


# 내가 한거 ,, 테스트는 통과 하지만 s와 p가 엄~~~청 긴 문장이결우 타임 오버가 나온다 
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        dict1 = {}
        dict2 = {}
        string = list(s)
        check = list(p)
        idx_last =len(string) - len(check)
        result = []

        lst = []

        for i in range(0,idx_last+1):
            check = list(p)
            for j in range(0,len(check)):
                if string[i] == check[j]:
                    lst.append(i)
                    break

        for i in check:
            if i not in dict1:
                dict1[i] = 1
            else :
                dict1[i] += 1
    
        for j in check:
            
            if j not in dict2:
                dict2[j] = 0
        

        for i in lst: 
            y = dict2.copy()
            copy = i 
            dict3 = y
            sucess = True
            for j in range(0,len(check)):
                if string[copy] not in dict1:
                    sucess = False
                    break
                elif string[copy] in dict1:
                    dict3[string[copy]] += 1
                    sucess = True
                copy = copy+1

            
            if sucess == True  and dict3 == dict1 :
                result.append(i)
        return result