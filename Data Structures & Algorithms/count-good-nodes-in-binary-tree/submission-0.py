# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        curr_path_max = [] # stack
        return self.findGoodNodes(root, curr_path_max)

    def findGoodNodes(self, node, stack):
        if node is None:
            return 0

        curr_max = stack[-1] if stack else -101
        is_good = node.val >= curr_max
        if is_good:
            stack.append(node.val)
        
        left_count = self.findGoodNodes(node.left, stack)
        right_count = self.findGoodNodes(node.right, stack)

        subtree_count = left_count + right_count
        if is_good: # our cur node had the max in its path up to it, so stack[-1] == node.val
            stack.pop()
            subtree_count += 1
        
        return subtree_count
        