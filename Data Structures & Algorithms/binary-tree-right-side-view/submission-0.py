# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.compute(root, 1, ans)
        return ans

    def compute(self, node, level, ans):
        if node is None:
            return

        if level > len(ans):
            ans.append(node.val)
        
        self.compute(node.right, level + 1, ans)
        self.compute(node.left, level + 1, ans)