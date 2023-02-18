
#1
# 중괄호 찾는 문제와 매우 비슷하다!
# ']'이 나오면 '['이 나올때 까지 pop한 후 [ 다음에 나오는 숫자만큼 반복한후 다시 stack에 push 해준다
# 스택에서 짝이 맞는 대괄호를 찾는다. 문자열에서 "]"이 발견되면 "["이 나올 때까지 뽑는다.
#  이후 "["을 찾으면 그 아래에는 "반복 횟수" k가 있으므로, 
#  앞서 발견한 문자열 패턴을 k회 반복한 것을 다시 스택에 올린다.
#   (주의) 반복 횟수 k는 여러 자리 자연수일 수 있다.

# 2
# k[encoded_string] 의 룰을 가진 문자열이 주어진다. 이 룰은 encoded_string 문자열을 k번 반복한다는 뜻이다.
# 룰은 중첩되서 나올 수 있다. k는 반드시 숫자이며 encoded_string에는 숫자가 포함되지 않는다.
# 위 룰을 적용한 문자열이 주어질 때 decode한 결과를 구하라.


# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"



# 장딥 
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, num, string = [], "", ""
        for char in s:
            if char == '[':
                stack.append(string)
                stack.append(num)
                string = ""
                num = ""
            elif char == ']':
                print("stack:{}".format(stack))
                prev_num = stack.pop()
                print("prev_num:{}".format(prev_num))
                prev_string = stack.pop()
                print("prev_string:{}".format(prev_string))
                string = prev_string + int(prev_num) * string
            elif char.isdigit():
                # + 하는 이유는 100[ab] 이런 경우도 있기 때문에 숫자유지를 위해서 사용
                num = num + char
                print("num:{}".format(num))
            else:
                string += char   
            print("string:{}".format(string))
        return string

# 비슷함 
class Solution(object):
    def decodeString(self, s):
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                # 이렇게 한 이유는 100[a]기준으로  1저장하고 다음은 10 다음은 100 이런식임 
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString


# 정답 정리 한것 같음 
class Solution(object):
    def decodeString(self, s):
        res = ""
        stack = []
        num = 0
        for i in s:
            print(stack)
            if i.isdigit():
                num = num*10+int(i)   
            
            elif i == "[":
                stack.append(res)
                stack.append(num)
                res = ""
                num = 0
            elif i == "]":
                n = stack.pop()
                r = stack.pop()
                res = r + n * res 
            else:
                res += i
                
        return res

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """


        result = ""    
        lst = list(s)
        intStack = []
        tmp = ""


        while len(lst) != 0:
            check = lst.pop(0)
            if check.isdigit():
                intStack.append(check)
            elif check == "[":
                tmp = ""
                while check != ']':
                    check = lst.pop(0)

                    if check.isdigit(): 
                        intStack.append(check)
                        check = lst.pop(0)
                        result = result + tmp
                        break
                    if check == ']': 
                        # tmp = tmp+check
                        break
                    tmp = tmp+check

                d = intStack.pop()
                print("d:{} , tmp:{}".format(d,tmp))
                result = result + (int(d) * tmp)

            elif check == "]":
                pass
            else :
                result = result + check
                # print(result)

        return result 
        # case 1 

        # cal = ""
        # result = ""
        # lst = list(s)
        # tmp = ""
        # # stack = []
        # intStack = []

        # while len(lst) != 0:
        #     check = lst.pop()

        #     if check.isdigit():
        #         # intStack.append(check)
        #         result = (int(check) * tmp) + result

        #     if check == "]":
        #         tmp =""
        #         while check != '[':
        #             check = lst.pop()
        #             if check != ']':
        #                 # tmp =""
        #                 pass
        #             if check !='[':
        #                 tmp = check + tmp

        #     if check == "[":
        #         check = lst.pop()
        #         print("result:{},check:{}".format(result,check))

        #         # number = intStack.pop()
        #         result = (int(check) * tmp) + result
        #         print(result)

        #     else:
        #         result = check + result 
            

        # return result

