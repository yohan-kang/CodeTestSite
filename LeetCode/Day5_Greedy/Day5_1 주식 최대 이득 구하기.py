# 해당 리스트에서 최소한으로 사고 최대한으로 파는 수를 리턴하는 문제 

# Example 2
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_buy = prices[0]
        max_sell = 0
        gain = 0
        
        for i in range(0,len(prices)-1) :

            if min_buy > prices[i]:
                min_buy = prices[i]

            # 전에는 if 를 추가해서 [7,6,4,3,1] 이 부분에 문제가 생김 : 그래서 if 문을 지워서 문제 해결 
            # if max_sell < prices[i+1]:
            max_sell = prices[i+1]

            # print(max_sell - min_buy)
            if (max_sell - min_buy) >= 0:
                if gain < (max_sell - min_buy):
                    gain = max_sell - min_buy

            # print("min_buy :",min_buy)
            # print("max_sell:",max_sell )
            # print("gain:",gain )

        return gain
        #return 0 if gain <= 0 else gain


# 아래것도 잘됨 
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_buy = prices[0]
        max_sell = 0
        gain = 0
        
        for i in range(0,len(prices)-1) :

            # if min_buy > prices[i]:
            #     min_buy = prices[i]
            # 위에 if 문 대신에 min으로 처리 
            min_buy = min (min_buy ,prices[i] )

            max_sell = prices[i+1]

            # if (max_sell - min_buy) >= 0:
                # if gain < (max_sell - min_buy):
                #     gain = max_sell - min_buy
            # 위에 if문 대신에 max로 처리 하지만 시간 복잡도에서는 어떻게 될지 모르곘다 
            gain = max(gain ,(max_sell - min_buy),0 )
        return gain