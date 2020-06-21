# 二分查找树
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        """不要老记着搞个什么哨兵头结点，老老实实搞个根结点，注意初始化情况就好了"""
        self.root = None

    def insert(self, value):
        # 初始化
        if self.root is None:
            self.root = TreeNode(value)
            # 注意这个返回终结，经常会遗漏，归根揭底没带脑子完完整整的走这个流程
            return
        p = self.root
        # 容易犯两个错误：1. 不带else 2. 循环终止未退出
        # while p is not None:
        #     if value < p.value:
        #         if p.left is None:
        #             p.left = TreeNode(value)
        #         else:
        #             p = p.left
        #     else:
        #         if p.right is None:
        #             p.right = TreeNode(value)
        #         else:
        #             p = p.right

        while p is not None:
            if value < p.value:
                if p.left is None:
                    p.left = TreeNode(value)
                    return
                p = p.left
            else:
                # 这个插入写法支持插入重复数据，只是搜索和删除时要注意存在重复分数据
                if p.right is None:
                    p.right = TreeNode(value)
                    return
                p = p.right

    def find(self, value):
        p = self.root
        while p is not None:
            if value < p.value:
                p = p.left
            elif value > p.value:
                p = p.right
            else:
                return p

        return None

    def find_larget_node(self):
        """最大结点，从右子树中找最右的子结点"""
        p = self.root
        if p is None:
            # 这里人为保证二叉树中没有-1，用-1来指代未找到
            return -1

        while p.right is not None:
            p = p.right

        return p.value

    def find_least_node(self):
        p = self.root
        if p is None:
            return -1

        while p.left is not None:
            p = p.left

        return p.value

    def delete(self, value):
        """不考虑重复值的情况"""
        # 1. 待删除结点是叶子结点
        # 2. 待删除结点只有一个子结点
        # 3. 待删除结点有两个子结点
        p = self.root
        pp = None
        while p is not None:
            pp = p
            if value < p.value:
                p = p.left
            elif value > p.value:
                p = p.right
            else:
                break

        if p.left is not None and p.right is not None:
            # 结点右子树中找最小的结点，做值替换和删除
            minp = p.right
            minpp = p
            while minp.left is not None:
                # 根本没想清楚，这里又错了
                # minp = minp.left
                # minpp = minp
                minpp = minp
                minp = minp.left
            p.value = minp.value
            p = minp
            pp = minpp

        # 这里提前找到待删除结点的子结点，免得后面执行删除时每个分支再次重复判断
        if p.left is not None:
            # 这个找child，如果有左子结点，优先左子结点的设计也是很有考究：before
            # 有个屁的考究，本来到这的待处理节点最多就只有一个左或右子节点，先左先右都一样：20200621
            child = p.left
        elif p.right is not None:
            child = p.right
        else:
            child = None

        # 这个假设待删除结点是根结点的设计也很巧妙，巧妙的通过初始化时假定根结点的父结点是None来实现判断
        if pp is None:
            self.root = child
        elif pp.left == p:
            pp.left = child
        else:
            pp.right = child

    def find_support_duplicate_node(self, value):
        """返回两个数组，结点数组与结点父数组，通过两个数组的索引将二者关联起来，比如pp_arr[0]和p_arr[0]为父子结点对"""
        pp_arr = []
        p_arr = []
        # 这个标识了删除的是根结点的情况
        pp = None
        p = self.root
        # 循环终止条件，老套路了
        while p is not None:
            if value < p.value:
                pp = p
                p = p.left
            elif value > p.value:
                pp = p
                p = p.right
            else:
                pp_arr.append(pp)
                p_arr.append(p)
                # 继续在右子树里查找，这是因为插入的时候把相同值的结点按照大于当前结点插入到右子树中去了。如果插入时插入到做左子树也可以
                # 但查找操作这里要同步处理
                pp = p
                p = p.right

        return pp_arr, p_arr

    def delete_support_duplicate_node(self, value):
        # 支持重复元素查找和删除的方法的删除操作的核心逻辑可以复用上面删除的部分，但是我这里还是单独把那部分重新写一个单独的功能函数出来
        # 仅仅是为了加强练习
        pp_arr, p_arr = self.find_support_duplicate_node(value)
        for i in range(len(p_arr) - 1, -1, -1):
            self.delete_base_method(p_arr[i], pp_arr[i])

        return 'Successfully delete ' + str(len(pp_arr)) + ' nodes!'

    def delete_base_method(self, p, pp):
        """删除指定结点，传参此结点与其父结点"""
        if p.left is not None and p.right is not None:
            # 找右子树中最小的结点，拿这个结点的值替换p结点（值替换，不是结点整体替换），然后删除这个最小结点
            # 删除这个最小结点有门道，肯定没有左子结点，那就只能是只有一个子结点或者没有子结点，这个直接可以使用外圈的逻辑
            minp = p.right
            minpp = p
            while minp.left is not None:
                minpp = minp
                minp = minp.left
            # 又专注局部逻辑了，光想着找右子结点的最小结点，忘了对p结点的值替换操作
            p.value = minp.value
            # 做替换，复用结点无子结点和只有一个子结点的删除逻辑
            p = minp
            pp = minpp

        # 找p的子结点，归根究底这个操作是将pp原来指向p的指针指向p的子结点（child可能存在也可能为None，没关系，None就当删除结点操作了）
        # 几个关键点：
        # 1. p是pp的左还是右子结点
        # 2. p的child子结点是什么，没有或者是左是右无所谓
        if p.left is not None:
            child = p.left
        elif p.right is not None:
            child = p.right
        else:
            child = None

        # 考虑p是根结点的情况
        # 树的边界条件删除根结点就是改变根结点root的指向
        if pp is None:
            self.root = child
        elif pp.left == p:
            pp.left = child
        else:
            pp.right = child

    def pre_order_traverse(self):
        if self.root is None:
            print('Warning: this is an empty tree')
            # 出错了，打印信息只是提示作用，当然要退出程序
            return

        self.pre_order_traverse_r(self.root)

    def pre_order_traverse_r(self, p):
        if p is None:
            return
        print(p.value)
        self.pre_order_traverse_r(p.left)
        self.pre_order_traverse_r(p.right)

    def in_order_traverse(self):
        if self.root is None:
            print('Warning: this is an empty tree')
            return

        self.in_order_traverse_r(self.root)

    # def in_order_traverse_r(self, p):
    #     # 结构化思维啊，写递归不给终止条件写个啥
    #     # 递归几要素：递推公式，终止条件
    #     self.in_order_traverse_r(p.left)
    #     print(p.value)
    #     self.in_order_traverse_r(p.right)

    def in_order_traverse_r(self, p):
        if p is None:
            return
        self.in_order_traverse_r(p.left)
        print(p.value)
        self.in_order_traverse_r(p.right)

    def post_order_traverse(self):
        if self.root is None:
            print('Warning: this is an empty tree')
            return

        self.post_order_traverse_r(self.root)

    def post_order_traverse_r(self, p):
        if p is None:
            return
        self.post_order_traverse_r(p.left)
        self.post_order_traverse_r(p.right)
        print(p.value)

    def traverse_by_layer(self):
        if self.root is None:
            print('Warning: this is an empty tree')
            return

        tq = deque([self.root])
        while tq:
            tn = tq.popleft()
            print(tn.value)
            if tn.left is not None:
                tq.append(tn.left)
            if tn.right is not None:
                tq.append(tn.right)


def test_no_duplicate_tree():
    bst = BinarySearchTree()
    bst.insert(33)
    bst.insert(17)
    bst.insert(50)
    bst.insert(13)
    bst.insert(18)
    bst.insert(34)
    bst.insert(58)
    bst.insert(16)
    # bst.in_order_traverse()
    # bst.pre_order_traverse()
    # bst.post_order_traverse()
    # print(bst.find(17).left.value)
    bst.insert(33)
    # bst.in_order_traverse()
    bst.traverse_by_layer()
    print(bst.delete_support_duplicate_node(50))
    bst.traverse_by_layer()
    print("find the larget and least node in bst: ")
    print(bst.find_larget_node())
    print(bst.find_least_node())


if __name__ == "__main__":
    test_no_duplicate_tree()