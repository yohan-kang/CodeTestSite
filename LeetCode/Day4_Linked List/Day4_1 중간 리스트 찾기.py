# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return ("val:{} , next:{}".format(self.val,self.next))
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # result = ListNode()
        # copy = result
        
        # if list1 is None:
        #     result = list2
        #     return result
        # if list2 is None:
        #     result = list1
        #     return result

             
        # while (list1 is not None) and (list2 is not None):
 
        #     if list1.val < list2.val :
        #         result.val = list1.val
        #         result.next = ListNode()
        #         list1 = list1.next
        #     else: 
        #         result.val = list2.val
        #         result.next = ListNode()
        #         list2= list2.next
            
        #     result = result.next
        #     # print(list1)
        #     # print(list2)
        
        # if list1 is None:
        #     result.val = list2.val
        #     result.next = list2.next
        #     # result = list2
        #     # print("마지막 안해요 list 2 ")
        #     return copy
        # if list2 is None:
        #     result.val = list1.val
        #     result.next = list1.next
        #     # result = list1
        #     # print("마지막 안해요? list 1 ")
        #     return copy
        # return copy
            
        if list1 == None or list2 == None:
            return list2 if list1 == None else list1
        
        head = None
        if list2.val <= list1.val:
            head = list2
            list2 = list2.next
        else:
            head = list1
            list1 = list1.next
        p = head

        while list1 != None and list2 != None:
            if list2.val <= list1.val:
                p.next = list2
                list2 = list2.next
            else:
                p.next = list1
                list1 = list1.next
            p = p.next
        
        if list1 == None:
            p.next = list2
        else:
            p.next = list1
        return head