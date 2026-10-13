# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = deque()
        queue.append(root)

        while queue:
            new_level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node is None:
                    continue
                new_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            if new_level:
                ans.append(new_level)
        return ans
