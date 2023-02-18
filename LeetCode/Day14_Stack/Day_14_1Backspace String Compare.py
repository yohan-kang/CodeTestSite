
# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

# 문자에 # 이 있으면 전에 문자를 제거한다 그리고 양쪽에 문자를 비교해서 일치하면 true를 리턴한다 

# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# Example 2:

# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
# Example 3:

# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b"


# Constraints:

# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.
 

# Follow up: Can you solve it in O(n) time and O(1) space?


class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        result1 = ""
        result2 = ""

        for i in range(0,len(s)):
            if s[i] != "#":
                result1 = result1+s[i]
            else:
                result1 = result1[:-1]


        for j in range(0,len(t)):
            if t[j] != "#":
                result2 = result2+t[j]
            else:
                result2 = result2[:-1]

        if result1 == result2:
            return True
        else :
            return False 



class Solution:
    def backspaceCompare(self, S, T):
        s, t = [], []
        for i in S: s = s + [i] if i != '#' else s[:-1]
        for i in T: t = t + [i] if i != '#' else t[:-1]
        return s == t