# 계단오르기 경우의 수 구하기 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step




# 피보나치 방법과 같이 적용했는데 속도가 엄청 느리다.... 
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        dict = {1:1,2:2}


        def fibo(n):
            if n in dict:
                return dict[n]

            result = fibo(n-1) + fibo(n-2)
            dict[n] = result
            print(dict)
            return result

            
        return fibo(n)