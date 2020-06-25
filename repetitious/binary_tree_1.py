# tree iteration traversal


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def construct_tree():
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(5)
    root.left.left.left.right = TreeNode(6)

    return root


def in_order_recur(root):
    if root is None:
        return

    in_order_recur(root.left)
    print(root.val)
    in_order_recur(root.right)


def in_order_iteration(root):
    tree_stack = []
    tree_list = []

    while tree_stack or root:
        while root:
            tree_stack.append(root)
            root = root.left

        node = tree_stack.pop()
        tree_list.append(node.val)
        root = node.right

    print(("\n".join(map(str, tree_list))))


if __name__ == "__main__":
    root = construct_tree()
    print("recursion: ")
    in_order_recur(root)
    print("iteration: ")
    in_order_iteration(root)