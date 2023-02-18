


# 제일 큰 수 2개를 빼면서 1이 될때까지 돌리는것 


# Example 1:

# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
# Example 2:

# Input: stones = [1]
# Output: 1





# 내가 한거 풀었지만 속도가  아쉽다 
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        lst = stones
        num = 0
        if len(lst) == 1:
            return lst[0]

        while len(lst) != 1 :
            lst.sort(reverse=True)
            if len(lst) != 2:
                num = lst[0]-lst[1]
                lst = lst[2:]
                lst.append(num)
            else : 
                num = lst[0]-lst[1]
                return num 



# 이거 깔끔하게 코드 잘짠것 같다 
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        while len(stones) > 1:
            l1 = max(stones)
            stones.remove(l1)
            l2 = max(stones)
            stones.remove(l2)
            if l1 < l2:
                stones.append(l2-l1)
            elif l1 > l2:
                stones.append(l1-l2)
            
        return stones[0] if stones else 0

# 이거 전체적으로 이해 더 잘감 
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if len(stones)==1:
            return stones[0]

        while(len(stones)!=1):
            m1 = max(stones)
            stones.remove(m1)
            m2 = max(stones)
            if(m1==m2):
                if(len(stones)==1):
                    return 0
                else:
                    stones.remove(m2)                
            elif(m2<m1):
                d = m1-m2
                stones.append(d)
                stones.remove(m2)

        return stones[0]
