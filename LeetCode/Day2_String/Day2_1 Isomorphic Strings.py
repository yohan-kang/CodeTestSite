

# 단어 동일한 형태인지 확인하는 문제 

# Example 1:

# Input: s = "egg", t = "add"
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# Output: false
# Example 3:

# Input: s = "paper", t = "title"
# Output: true

# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.



class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # dic = {}

        # if len(s) != len(t):
        #     return False

        # for i in range(0,len(s)): 
        #     if s[i] in dic: 
        #         if dic[s[i]] != t[i]:
        #             return False

        #     if t[i] in dic.values():
        #         for key, value in dic.items():
        #             if t[i] == value:
        #                 if key != s[i]:
        #                     return False
        #     dic[s[i]] = t[i]
        # return True

        one_dy = {} 
        two_dy = {}
        if len(s) != len(t):
            return False

        for i in range(0,len(s)):
            if s[i] in one_dy:
                if one_dy[s[i]] != t[i]:
                    return False
            if t[i] in two_dy:
                if two_dy[t[i]] != s[i]:
                    return False
            one_dy[s[i]] = t[i]
            two_dy[t[i]] = s[i] 

        return True


# case 루이 
        dic_s = {}
        dic_t = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if dic_s.setdefault(s[i],t[i]) != t[i] or dic_t.setdefault(t[i],s[i]) != s[i]:
                return False
        return True

