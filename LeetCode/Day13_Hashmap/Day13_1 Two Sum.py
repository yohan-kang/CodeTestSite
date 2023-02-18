# 정수가 담긴 리스트와 타깃 정수가 주어지고 리스트에서 2개를 골라 더해서 타깃 정수가 되면 해당 수들의 index값을 반환하면 되는 문제입니다.
#  하나의 케이스에는 정확히 답 하나만이 존재한다고 합니다. 그리고 index를 반환할 떄의 순서는 상관없습니다.

#  Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


# n 제곱으로 일단 실행 해봄  하지만 n제곱으로 비효율적 
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """


        ln = len(nums)
        print(ln)
        result = []

        for i in range(0,ln-1) :
            for j in range(i+1,ln) :
                if int(nums[i] + nums[j]) == target:
                    result.append([i , j])
                    return result[0]

# 맵 이용하기 
class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            d[num] = i
        return []

# ex [5,2,4,9] target 13 

# d[5] = 0
# d[2] = 1
# d[4] =2
# d[13- 9] == d[4]  
# [2 ,3]

# 직접 해봄 
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """


        dict = {}

        for i in range(0, len(nums)):
            if nums[i] in dict:
                return [dict[nums[i]],i]
            dict[target-nums[i]] = i
        return []