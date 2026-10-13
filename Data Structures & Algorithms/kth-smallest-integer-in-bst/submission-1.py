# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count, ans = self.search(root, k, 0)
        return ans

    def search(self, node, k, count):
        if node is None:
            return count, None

        count, found_node = self.search(node.left, k, count)
        if found_node is not None:
            return count, found_node
        
        count += 1
        if count == k:
            return count, node.val

        count, found_node = self.search(node.right, k, count)
        if found_node is not None:
            return count, found_node

        return count, None
