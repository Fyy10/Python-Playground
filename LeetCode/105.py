from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        
        root = TreeNode()
        root.val = preorder[0]

        idx_in = inorder.index(root.val)
        inorder_left = inorder[: idx_in]
        inorder_right = inorder[idx_in + 1:]

        idx_pre = len(inorder_left)
        preorder_left = preorder[1: idx_pre + 1]
        preorder_right = preorder[idx_pre + 1:]

        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root
