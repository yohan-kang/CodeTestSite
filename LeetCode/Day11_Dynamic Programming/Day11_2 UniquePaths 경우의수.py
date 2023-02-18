


# 행과 열을 주고 0,0 에서 마지막 행열 까지 가는 경우의 수 구하기 문제이다 

# Example 1:


# Input: m = 3, n = 7
# Output: 28
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down




# 이 문제의 핵심은 결국 경우의 수는 원하는 마지막 해당 위치에서 왼쪽과 위쪽에 도착하는 경우의 수를 더해주면 된다 
# 즉 특정 칸까지 가는 경로의 수는 위의 칸까지 가는 경로의 수와 왼쪽 칸까지 가능 경로의 수의 합과 같다.
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        result = 0
        row = m
        col = n 
        j = 1
        j = 1 

        lst = [[1]*col for i in range(row)]


        # 행과 열 둘중 하나라도 1이면 한줄이기때문에 경의수가 하나이기 때문에 리턴1을 추가해준다 
        if col == 1 or row ==1 :
            return 1 

        for i in range(1,row):
            global i,j
            for j in range(1,col):
                lst[i][j] = lst[i-1][j] + lst[i][j-1]
        # print("i:{},j:{}".format(i,j))
        return  lst[i][j]
