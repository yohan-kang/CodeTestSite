# Example 1:


# Input: root = [2,1,3]
# Output: true
# Example 2:


# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
 

# 두번째꺼는 5의 자식 으론쪽은 자신보다 커야 하는데 4가 있어서 잘못된 노드이다 


# 이건 우선순위 아니어서 안품 그냥 정답만 


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.bst(float('-inf'),float('inf'),root)
        
    def bst(self,low,high,node):
        if not node:
            return True
        if not (low<node.val<high):
            return False
        return self.bst(low,node.val,node.left) and self.bst(node.val,high,node.right)

# 제일 빠른 정답 
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = []

        # in order traversal returns sorted array if valid binary search tree
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)

        for i in range(1, len(res)):
            if res[i] <= res[i-1]:
                return False
        
        return True