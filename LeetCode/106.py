from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        root = TreeNode()
        if len(postorder) == 0:
            root = None
            return root
        else:
            root.val = postorder[-1]

        idx_in = inorder.index(root.val)
        inorder_left = inorder[:idx_in]
        inorder_right = inorder[idx_in + 1:]

        idx_post = len(inorder_left)
        postorder_left = postorder[:idx_post]
        postorder_right = postorder[idx_post: -1]

        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        return root
