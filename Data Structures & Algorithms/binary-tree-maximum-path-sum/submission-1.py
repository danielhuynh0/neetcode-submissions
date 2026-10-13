# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val
        def compute(node):
            nonlocal ans

            if node is None:
                return 0

            left_max = compute(node.left)
            right_max = compute(node.right)

            cur = node.val
            cur = left_max + cur if left_max + cur > cur else cur
            cur = right_max + cur if right_max + cur > cur else cur
            ans = max(ans, cur)
            return max(left_max, right_max, 0) + node.val
        
        compute(root)
        return ans
    