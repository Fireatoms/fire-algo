# binary search tree
# core operations
# 1. search node in bft
# 2. insert node
# 3. remove node


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTreeNoDuplication:
    """in order to simplify operations, let's assume that there is no duplicate data in bst"""
    def __init__(self, node=None):
        self.root = node

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
            return

        root = self.root
        # that while True is also ok because when root become None, the loop will terminate immediately
        # while True:
        while root:
            if data < root.val:
                if root.left is None:
                    root.left = TreeNode(data)
                    return
                root = root.left
            else:
                if root.right is None:
                    root.right = TreeNode(data)
                    return
                root = root.right

    def search(self, data):
        root = self.root

        while root:
            if data < root.val:
                root = root.left
            elif data > root.val:
                root = root.right
            else:
                return root

        return None

    def remove(self, data):
        """we must get the node to be removed and its parent node"""
        pp = None
        p = self.root

        while p:
            if data < p.val:
                pp = p
                p = p.left
            elif data > p.val:
                pp = p
                p = p.right
            else:
                break

        if p is None:
            return False

        if p.left and p.right:
            # 1. find min node minp in right subtree and its parent node minpp
            # 2. replace p val with minp val
            # 3. pp = minpp p = minp to use the removal mechanism below
            minpp = p
            minp = p.right
            while minp.left:
                minpp = minp
                minp = minp.left

            p.val = minp.val
            pp = minpp
            p = minp

        # tips: get the child node of p: None, left node or right node
        # then let the pointer that originally pointed to p point to its child
        if p.right:
            child = p.right
        elif p.left:
            child = p.left
        else:
            child = None

        # let the pointer of pp which point to p point to child
        if pp is None:
            # Considering the actual situation, removing the root node is a special case
            # From the perspective of writing code, it is a special case that pp is None
            self.root = child
        elif pp.left == p:
            pp.left = child
        else:
            pp.right = child

        return True

    def find_largest_node(self):
        root = self.root
        while root.right:
            root = root.right

        return root

    def find_smallest_node(self):
        root = self.root
        while root.left:
            root = root.left

        return root

    def find_pre_node(self, data):
        p = self.root
        pp = None

        while p:
            if data < p.val:
                pp = p
                p = p.left
            elif data > p.val:
                pp = p
                p = p.right
            else:
                return pp

        return None

    def find_post_node(self, data):
        p = self.root
        pc = [None, None]

        while p:
            if data < p.val:
                p = p.left
            elif data > p.val:
                p = p.right
            else:
                pc = [p.left, p.right]
                break

        return pc

    def search_support_duplicate_node(self, data):
        """In order to make it more convenient to delete nodes, we let this func return nodes and there parent nodes"""
        p = self.root
        pp = None
        node_arr = []
        parent_node_arr = []

        while p:
            if data < p.val:
                pp = p
                p = p.left
            elif data > p.val:
                pp = p
                p = p.right
            else:
                node_arr.append(p)
                parent_node_arr.append(pp)
                pp = p
                p = p.right

        return node_arr, parent_node_arr

    def remove_node(self, p, pp):
        """remove given node"""
        if p.left and p.right:
            minpp = p
            minp = p.right

            while minp.left:
                minpp = minp
                minp = minp.left

            p.val = minp.val
            pp = minpp
            p = minp

        if p.left:
            child = p.left
        elif p.right:
            child = p.right
        else:
            child = None

        if pp is None:
            self.root = child
        elif pp.left == p:
            pp.left = child
        else:
            pp.right = child

    def remove_support_duplicate_node(self, data):
        p_arr, pp_arr = self.search_support_duplicate_node(data)
        # it is wrong that remove node from up to down because remove the node above may
        # change the status of the node blew
        # for example: 33 17 50 13 25 33 37, if you run the simulation, it is easy to see  that the root 33 node
        # will not be removed.
        # for i in range(len(p_arr)):
        #     self.remove_node(p_arr[i], pp_arr[i])
        for i in range(len(p_arr)-1, -1, -1):
            self.remove_node(p_arr[i], pp_arr[i])


def construct_bst():
    bst = BinarySearchTreeNoDuplication()
    bst.insert(33)
    bst.insert(17)
    bst.insert(50)
    bst.insert(13)
    bst.insert(25)

    return bst


def in_traversal(root):
    if root is None:
        return

    in_traversal(root.left)
    print(root.val)
    in_traversal(root.right)


if __name__ == "__main__":
    bst = construct_bst()
    bst.insert(33)
    bst.insert(37)
    # node_arr, parent_node_arr = bst.search_support_duplicate_node(33)
    # print(node_arr)
    # print(parent_node_arr)
    bst.remove_support_duplicate_node(33)
    in_traversal(bst.root)
    # in_traversal(bst.root)
    # print('\n')
    # bst.insert(2)
    # la = bst.find_largest_node()
    # print(la.val)
    # print(bst.find_smallest_node().val)
    # print(bst.find_pre_node(33))
    # print(bst.find_pre_node(17).val)
    # pc = bst.find_post_node(33)
    # print(pc[0].val, pc[1].val)
    # in_traversal(bst.root)
    # res = bst.search(33)
    # print(res.left.val)
    # print(res.right.val)
    # bst.remove(50)
    # in_traversal(bst.root)
    # bst.remove(33)
    # in_traversal(bst.root)
