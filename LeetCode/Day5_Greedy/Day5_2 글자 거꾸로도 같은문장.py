class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        dic = {}
        flus_mid = 0
        odd_num = 0
        even_num = 0
        
        for i in s:

            if i in dic:
                dic[i] = int(dic[i])+1
            else:
                dic[i] = 1

        for i in dic:

            if dic[i] % 2 == 0:
                even_num= even_num + dic[i]
            else :
                odd_num = odd_num + dic[i] -1
                flus_mid = 1
        
        return odd_num + even_num + flus_mid

        # 루이가 성공한 방법    홀수는 1은 0으로 만들고 1이상의 홀수는 -1을 한 값을 더해준다  그리고 홀수가 하나라도 있는경우 마지막에 하나 추가해준다 
        # dic = {}
        # for c in s:
        #     dic[c] = dic.setdefault(c,0) + 1
        # sum = 0
        # biggest_odd_number = 1
        # for val in dic.values():
        #     if val % 2 == 0:
        #         sum += val
        #     else:
        #         sum += val -1
        #         biggest_odd_number = 1
            
        # print(dic)
        # return sum+biggest_odd_number
        



        # 빠른 방법 1번
        # tore_dic = dict()
        # for single_str in s:
        #     if single_str in store_dic:
        #         del store_dic[single_str]
        #     else:
        #         store_dic[single_str] = 1

        # if len(store_dic) == 0:
        #     return len(s) - len(store_dic)
        # else:
        #     return len(s) - len(store_dic) + 1