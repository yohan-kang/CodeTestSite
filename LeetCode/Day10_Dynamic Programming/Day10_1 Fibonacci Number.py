




# 피보나치 수를 구하라
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.

# Example 1:

# Input: n = 2 Output: 1 Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

# Example 2:

# Input: n = 3 Output: 2 Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

# Example 3:

# Input: n = 4 Output: 3 Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.


# 끝났다 짐싸라 이게 정답중에 정답이다 
def staircase(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a




# 처음 시도한거  근데 속도 완전 느리다 재귀 방식의 Top-Down(하향식) 풀이이다.
# 코드는 간결하나 중복된 계산을 하여 성능이 좋지 않다.
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """        
        if n > 1:
            
            return self.fib(n-1)+self.fib(n-2)
        else :
            if n == 1:
                return 1
            if n == 0:
                return 0 

# 똑같은 허접 코드 
        # def helper(n):
        #     if n == 0:
        #         return 0
        #     elif n == 1:
        #         return 1
        #     else:
        #         return helper(n - 1) + helper(n - 2)
        # return helper(n)

# ~~~~~~ 여기가 내가 아래 모든 부분을 참고하여 수정한 최종 답안  - 개빠름
        dict = {0:0 ,1:1}
        
        def fibo(n) :

            if n in dict:
                return dict[n]
            # else :? 

            result = fibo(n-1) + fibo(n-2)
            dict[n] = result
            return result
                
                
        if 0<=n and n<= 30:
            return fibo(n)



# 조금 느리지만 내가생각하기엔 조건에 맞는 완벽한 답안이다 
def sum (n):
    if n == 2:
        return 1
    elif n == 1:
        return 1
    return sum(n-1) + sum(n-2)

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0 or n > 30:
            return 0
        return sum(n)

# 사람들이 올린 블로그  메모이제이션 방식 풀이 계산한 값은 딕트에 저장하여 중복된 계산을 하지 않는다. -> 성능이 10배가량 좋아졌다.
class Solution:
    dp = collections.defaultdict(int)
    
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        if self.dp[n]:
            return self.dp[n]
        # 중복된 계산을 하지않기 위해 계산한 값은 저장
        self.dp[n] = self.fib(n-2) + self.fib(n-1)
        
        return self.dp[n]



# 빠른거? 
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = {0:0, 1:1}

        def fibonaci(num):
            if num in d:
                return d[num]
            # if num == 1:

            val = fibonaci(num-1) + fibonaci(num-2)
            d[num] = val
            return val

        return fibonaci(n)

# 두번째로 빠른거 
    def fib(self, n):
        if n==0: return 0
        elif n==1: return 1
        
        A = [0 for i in range(n)]
        A[0]=0
        A[1]=1
        for i in range(2,n,1):
            A[i]= A[i-1]+A[i-2]
        return (A[n-1]+A[n-2])