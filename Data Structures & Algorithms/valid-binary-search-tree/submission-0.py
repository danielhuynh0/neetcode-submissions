# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        is_valid, _, _ = self.validate(root)
        return is_valid

    def validate(self, node: TreeNode):
        if node is None:
            return True, float("inf"), float("-inf")
        
        is_valid_left, min_left, max_left = self.validate(node.left)
        if not is_valid_left:
            return False, float("inf"), float("-inf")
        is_valid_right, min_right, max_right = self.validate(node.right)
        if not is_valid_right:
            return False, float("inf"), float("-inf")

        if max_left >= node.val:
            return False, float("inf"), float("-inf")
        if min_right <= node.val:
            return False, float("inf"), float("-inf")
        
        return True, min(min_left, node.val), max(max_right, node.val)