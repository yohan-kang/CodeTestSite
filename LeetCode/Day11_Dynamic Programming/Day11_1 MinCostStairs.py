# 여기서 cost[i]는 계단에서 계단을 밟는 비용인 정수 배열 비용이 제공됩니다. 일단 비용을 지불하면, 당신은 한 계단 또는 두 계단을 오를 수 있다.

# 인덱스가 0인 단계부터 시작하거나 인덱스가 1인 단계부터 시작할 수 있습니다.

# 바닥 꼭대기에 도달하기 위한 최소 비용을 반환합니ek 
# 0이나 1 인덱스로 시작해서 배열의 마지막을 넘어서야 한다 단 가장 최소의 비용으로 도달해야한다 
# Example 1:

# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.
# Example 2:

# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.
 

# Constraints:

# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999

# 이문제 결국 못품 



# 블로그 정답 참고함 
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total_count = len(cost)
        min_cost = [0] * (total_count+1)
        
        for i in range(2, total_count + 1):
            one_step = min_cost[i-1] + cost[i-1]
            two_step = min_cost[i-2] + cost[i-2]
            min_cost[i] = min(one_step, two_step)

        return min_cost[total_count]



class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)
        for i in range(2, len(cost)):
            cost[i] = cost[i] + min(cost[i - 1], cost[i - 2])

        return cost[i] 




class Solution(object):

    def minCostClimbingStairs(self, cost):

        l1 =0
        l2 =0

        for c in cost:
            l2, l1 = l1, min(l1, l2) + c
        return min(l2, l1)


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        first = cost[0]
        second = cost[1]
        for i in range(2, len(cost)):
            curr = cost[i] + min(first, second)
            first = second
            second = curr
        return min(first, second)