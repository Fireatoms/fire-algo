# binary_tree
# 基于链表的链式存储法构造二叉树
# 前序遍历：preorder 中序遍历：inorder 后续遍历：postorder 按层遍历
from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, value=0):
        self.root = TreeNode(value)

    def construct_test_tree(self):
        """构造一个测试用二叉树"""
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(3)
        self.root.left.left = TreeNode(4)
        self.root.left.right = TreeNode(5)
        self.root.right.left = TreeNode(6)
        self.root.right.right = TreeNode(7)


# 遍历的方法也可以写到二叉树类里，这里写成外部函数接受根节点作为输入
def pre_order(root):
    """递归哦，还是要继续思考整体逻辑"""
    if root is None:
        return
    print(root.value)
    pre_order(root.left)
    pre_order(root.right)


def in_order(root):
    """终止条件都应该是输入为None"""
    if root is None:
        return
    in_order(root.left)
    print(root.value)
    in_order(root.right)


def post_order(root):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.value)


def traverse_by_layer(root):
    """借助python的内置队列数据结构实现层遍历，bfs广度优先"""
    dt = deque([root])
    while dt:
        tree_node = dt.popleft()
        print(tree_node.value)
        if tree_node.left:
            dt.append(tree_node.left)
        if tree_node.right:
            dt.append(tree_node.right)


if __name__ == "__main__":
    bt = BinaryTree(1)
    bt.construct_test_tree()
    print("pre_order: ")
    pre_order(bt.root)
    print("in_order: ")
    in_order(bt.root)
    print("post_order: ")
    post_order(bt.root)
    print("traverse by layer: ")
    traverse_by_layer(bt.root)

