# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    ans = []

    # fill in ans
    def dfs(self, root, depth):
        # null node, exit
        if root is None:
            return

        # a new level
        if len(self.ans) <= depth:
            self.ans.append([root.val])
        else:
            # append to current level
            self.ans[depth].append(root.val)

        # left child
        self.dfs(root.left, depth + 1)
        # right child
        self.dfs(root.right, depth + 1)

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        # remember to reset ans!
        self.ans = []

        # start from root, level 0
        self.dfs(root, 0)

        return self.ans
