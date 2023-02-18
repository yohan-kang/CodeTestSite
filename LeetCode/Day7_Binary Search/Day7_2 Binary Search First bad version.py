# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

# Example 1:

# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.
# Example 2:

# Input: n = 1, bad = 1
# Output: 1

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """




        # 1처음엔 그냥 하나씩 체그하는 방법으로 함 , 하지만 시간이 오래걸림 
        # std = isBadVersion(n)
        # if std :
        #     while std is not False:
        #         n = n-1
        #         std = isBadVersion(n)
        #     return n+1
        # else: 
        #     while std :
        #         n = n+1
        #         std = isBadVersion(n)
        #     return n-1


        # 2리스트를 사용했다가 메모리초과로 문제가 있음
        # idx = n+1 
        # lst = list(range(1,idx))
        # mid = (len(lst)-1) //2

        # if len(lst) == 1 :
        #     return lst[0]
       
        # while len(lst)  > 1 : 
        #     mid = (len(lst)-1)//2
        #     if isBadVersion(lst[mid]):
        #         lst = lst[0:mid+1]
        #     else : 
        #         lst = lst[mid+1:idx]

        #         if mid == 0:
        #             if isBadVersion(lst[mid]) == False:
        #                 return lst[mid+1]
        #             else :
        #                 return lst[mid]
        #     # 1,4 case
        #     if len(lst) == 1:
        #         print(lst)
        #         if lst[0] == False:
        #             return lst[0]+1
        #         return lst[0]


        # 3case1  memory 를 고려하여 리스트 없이 코드 작성  하지만 매번 if 검사가 많아서 좋지 않음 
        left = 1
        right = n 
        mid =  (left+right) // 2

        while left - right != 1 :

            mid =(left+right) // 2
            if isBadVersion(mid):
                right = mid
            else :
                left = mid +1

            if (right-left) == 1:
                if isBadVersion(left):
                    return left
                else :
                    return right

            if (right-left) == 0:
                return left


# 가장 빠른 방법

class Solution(object):
    def firstBadVersion(self, n):
        low = 0
        high = n
        while low < high:
            mid = (low+high)//2

            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return high

# 빠른 경우 코드 보면서 리펙토링함 
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low=1
        high=n
        mid=(low+high)//2
        while low<=high:
            mid=(low+high)//2 # 중복 하나로 하기
            if isBadVersion(mid):
                high=mid-1
                # mid=(low+high)//2
            else:
                low=mid+1
                # mid=(low+high)//2
        if isBadVersion(low):
            return low
        # 이거 else 지워도 작동한다 명심  ~~~~~~~~~    
        else:
            return high