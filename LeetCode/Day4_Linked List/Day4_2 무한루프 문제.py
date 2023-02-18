class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

# 하나의 리스트가 있고 tail이 있는지 없는지 모르는 상황 여기서 마지막 노드에 tail이 전에 있는 노드와 연결되어 있으면 무한 루프로 되는데 이런경우
# 무한 루프의 첫 인덱스를 가진 노드를 리턴한다 



# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

# Do not modify the linked list.


# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.
# Example 2:


# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.



        # 나는 못풀었음 


        # 141

        # set
        # 2(a + b) = a + b + c + b => a = c
        # fast = 2 * slow

        if not head or not head.next:
            return None
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if not fast or not fast.next:
            return None
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next


# 내  사수 루이 풀이    하지만 시간이 제일 느림 !!! 
        if head is None:
            return None
        target = head.next
        prev_count = 0
        while target is not None:
            node = head
            pos = 0
            while node != target:
                pos += 1
                node = node.next
            if pos <= prev_count:
                return node
            prev_count = pos
            target = target.next
        return None
