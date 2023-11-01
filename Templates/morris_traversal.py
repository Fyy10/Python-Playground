from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# inorder traversal using Morris traversal
def morris_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    Inorder traversal of the tree with constant space,
    will modify the structure of the tree

    Args:
        root: root of the tree
    Returns:
        inorder traversal of the tree
    """
    inorder_traversal = []

    node = root
    while node:
        while node.left:
            friend = node.left
            while friend.right:
                friend = friend.right
            friend.right = node
            prev = node
            node = node.left
            prev.left = None

        # every time we get here, we get a new node inorder
        inorder_traversal.append(node.val)

        node = node.right

    return inorder_traversal


if __name__ == '__main__':
    # 1 -> [2, 3]
    # 2 -> [None, 4]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)

    # [2, 4, 1, 3]
    print(morris_traversal(root))
