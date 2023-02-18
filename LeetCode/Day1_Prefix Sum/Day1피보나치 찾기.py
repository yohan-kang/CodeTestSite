
# integer 배열 nums가 주어지고, "pivot" 인덱스를 해당 배열에서 찾아라.

# "pivot" 인덱스는 해당 인덱스를 기준으로 오른쪽 배열의 값들의 합과 왼쪽 배열의 값들의 합이 같은 경우를 말한다.

# 만약, 배열의 첫 번째 인덱스가 pivot이라면 왼쪽 배열의 합은 0이다, 왜냐하면 왼쪽에는 아무 배열도 없기 때문이다.

# 오른쪽도 마찬가지다.

# 가장 왼쪽에 위치하는 pivot 인덱스를 반환하라. 만약 존재하지 않는다면 -1을 반환하라.

# Example 1:

# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11
# Example 2:

# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.
# Example 3:

# Input: nums = [2,1,-1]
# Output: 0
# Explanation:
# The pivot index is 0.
# Left sum = 0 (no elements to the left of index 0)
# Right sum = nums[1] + nums[2] = 1 + -1 = 0


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

    #case 4
        sum_right = sum(nums)
        sum_left = 0
        pivot_index = 0
        while pivot_index <= len(nums)-1:
            sum_right -= nums[pivot_index]
            if sum_left != sum_right:
                sum_left += nums[pivot_index]
                pivot_index += 1
            else:
                return pivot_index
        return -1
        

    # case 3
    # # def pivotIndex(self, nums: list[int])-> int:
    #     pivot_index = 0 
    #     while 0 <= pivot_index and pivot_index < len(nums):
    #         sum_left = sum(nums[:pivot_index])
    #         sum_right = sum(nums[pivot_index+1:])
    #         if sum_left != sum_right:
    #             pivot_index += 1
    #         else:
    #             return pivot_index
    #     return -1

# 너 피폿인지 아닌지 일일이 체그할게 아니라 법뮈를 좁혀서 찾아봐라 성민님힌트 
# 각각이 피펏인지 아닌지 보면 안된다 

        # total = 0
        # for i in range(1,len(nums)):
        #     total= total+nums[i]
        
        # print(total)
        # left = 0
        # right = total
        # for i in range(0,len(nums)):
        #     if left == right :
        #         return i
        #     left = left + nums[i]
        #     if i != len(nums) -1:
        #         right = right - nums[i+1]
        #     else:
        #         right = right - nums[-1]
        #     # print( "left :{}, right: {}".format(left,right))
        # return -1   






        # # case 1  타임오버나옴
        # result = -1
        # left = 0

        # for i in range(0,len(nums)-1):
        #     right = 0
            
        #     for j in range(i+1,len(nums)):
                
        #         # 왼쪽오른쪽 합이 일치하지 않으면 오른쪽 값 더하기 
        #         right += nums[j]

        #         if j != len(nums) - 1 :
        #             continue
                
        #         # 조건 비교해보기
        #         if right == left:
        #             result = i
        #             break
                

        #     # 2차 반복문이 끝났으면 왼쪽 맥스값 올리기 
        #     print( "left :{}, right: {} , result : {}".format(left,right,result))
        #     left +=  nums[i]
            
        #     if result > -1 :
        #         return result

        
        # right = 0
        # print( "left :{}, right: {} , result : {}".format(left,right,result))
        # # right = 0

        # if right == left:
        #     result = len(nums)-1
        #     return result

        
        # # 모두 실패했을경우 
        # return -1


