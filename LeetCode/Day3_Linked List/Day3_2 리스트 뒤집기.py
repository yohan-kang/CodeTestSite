# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Input: head = [1,2]
# Output: [2,1]

# Input: head = []
# Output: []


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return ("val:{} , next:{}".format(self.val,self.next))
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

# 이것도 개쩐다 
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        inv_head = None
        while head:
            inv_head = ListNode(head.val, inv_head)
            head = head.next
        
        return inv_head

# 완벽한 답안 
class Solution: 
    def reverseList(self,head):
        prev = None
        while head!=None:
            temp=head
            head=head.next
            temp.next=prev
            prev=temp
        return prev


# 다른건데 ,,, 아주 느리다
class Solution(object):

    def reverseList(self, head):

        previous_node = None
        while head:
            next_node = head.next
            head.next = previous_node
            previous_node = head
            head = next_node
        return previous_node


# 루이 답안 
# class Solution:
#     def reverseList(self,head):
#         if head == None:
#             return None
#         if head.next == None:
#             return head
#         p = head
#         p_next = p.next
#         head.next = None
#         while p_next != None:
#             p_next_next = p_next.next
#             p_next.next = p
#             p = p_next
#             p_next = p_next_next
#         return p


# 실패함 
        # lst = []
        # result = ListNode()
        # copy = result

        # if head is None :
        #     return result


        # while head.next is not None:
        #     lst.append(head)
        #     head = head.next
        # lst.append(head)
        # print(len(lst))


        # for i in range(len(lst)-1,-1,-1):
        #     result.val = lst[i].val
        #     result.next = lst[i]

        #     if i == 0:
        #         result.val = lst[i]
        #         result.next = None
        #     result = result.next
        # return copy
