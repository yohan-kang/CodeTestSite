# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 # 레벨 별로 리스트 묶어서 분류한다 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []





# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 처음 시도 한거  근데 속도가 많이 느리다 
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        # [] case return None 
        if root is None:
            return None

        result=[[root.val]]
        level_lst = []

        parent_que = []
        child_que = []
        
        parent_que.append(root)

        while len(parent_que) != 0 :
            target = parent_que.pop(0)
            if target.left is not None:
                child_que.append(target.left)
                level_lst.append(target.left.val)
                print(level_lst)
            if target.right is not None: 
                child_que.append(target.right)
                level_lst.append(target.right.val)
                print(level_lst)
            # que,list reset part 
            if len(parent_que) == 0:
                parent_que = child_que
                child_que = []
                if len(level_lst) != 0:
                    result.append(level_lst)
                    level_lst = []
        return result

