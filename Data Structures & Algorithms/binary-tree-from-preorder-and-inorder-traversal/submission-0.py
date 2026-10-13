# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val:idx for idx,val in enumerate(inorder)}

        def construct(startP, endP, startI, endI):
            if startP >= endP or startI >= endI:
                return None

            root = preorder[startP]
            rootNode = TreeNode(root)
            
            rootIdx = idx_map[root]
            left_tree_count = rootIdx - startI
            rootNode.left = construct(startP+1, startP+left_tree_count+1, startI, rootIdx)
            rootNode.right = construct(startP+left_tree_count+1, endP, rootIdx+1, endI)

            return rootNode
        
        return construct(0, len(preorder), 0, len(inorder))
