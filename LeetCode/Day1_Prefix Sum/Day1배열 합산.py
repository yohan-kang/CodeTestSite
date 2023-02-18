# 배열 번호가 지정되었습니다. 배열의 실행 합계를 실행 중인 Sum[i] = sum(nums[0]…nums[i])으로 정의합니다.
# 실행 중인 숫자의 합계를 반환합니다.
# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Example 2:

# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
# Example 3:

# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]



class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rlist = []
        result = 0
        for i in nums:
            result += i
            rlist.append(result)

        return rlist


# Runtime
# 25 ms
# Beats
# 75.91%

# Memory
# 13.6 MB
# Beats
# 68.12%