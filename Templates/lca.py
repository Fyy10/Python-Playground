# lowest common ancestor
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lca(root: Node, p: Node, q: Node) -> Node:
    """
    Given a tree root and two nodes on the tree, return the
    lowest common ancestor of the two nodes.

    Args:
        root (Node): tree root
        p (Node): node 1
        q (Node): node 2

    Returns: the lowest common ancestor of the two nodes
    """
    if root == p or root == q:
        return root

    if root.left:
        l = lca(root.left, p, q)
    else:
        l = None

    if root.right:
        r = lca(root.right, p, q)
    else:
        r = None

    if l and r:
        return root
    return l or r
