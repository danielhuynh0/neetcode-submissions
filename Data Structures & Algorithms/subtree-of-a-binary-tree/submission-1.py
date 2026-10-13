# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None and subRoot == None:
            return True
        return self.findSubRoot(root, subRoot)

    def findSubRoot(self, root, subRoot):
        if root == None:
            return False
        
        left = self.findSubRoot(root.left, subRoot)
        right = self.findSubRoot(root.right, subRoot)
        if left or right:
            return True

        if root.val == subRoot.val:
            return self.isSameTree(root, subRoot)
        
        return False

    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        if not left or not right:
            return False
        
        return True if p.val == q.val else False