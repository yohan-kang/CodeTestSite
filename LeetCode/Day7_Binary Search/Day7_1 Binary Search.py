# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 


# 배열과 숫자하나를 파라미터로 준다면   내어준 숫하 나가의 값이 배열안에 있다며 해당 배열의 인덱스를 리턴한다 


# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1




# 내가 한거 
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.left = 0
        self.right = len(nums) - 1
        
        while self.left <= self.right:
            self.mid = (self.left + self.right) // 2
            if nums[self.mid] == target:
                return self.mid
            elif nums[self.mid] > target:
                self.right = self.mid - 1
            else:
                self.left = self.mid + 1
        return -1



# 가장빠른정답 
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # for i in range(0,len(nums)):
        #     if target == nums[i]:
        #         return i
        # return -1


        idx_lst = []

        if len(nums) == 0 :
            return -1
        
        for i in range(0,len(nums)):
            idx_lst.append(i)

        while len(idx_lst) != 0 :
            mid = (len(idx_lst) // 2)
            if nums[idx_lst[mid]] == target:
                return idx_lst[mid]
            if nums[idx_lst[mid]] < target:
                idx_lst = idx_lst[mid+1:] 
            else :
                idx_lst = idx_lst[:mid] 
        return -1  

# 괜찮아 보임
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m -1
            else:
                l = m + 1

        return -1