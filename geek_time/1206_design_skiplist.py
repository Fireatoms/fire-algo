# link: https://leetcode-cn.com/problems/design-skiplist/
import random


class Node:
    def __init__(self, val=0, index_level=0):
        self.val = val
        # 索引层数，不含原始数据层
        self.index_level = index_level
        # 每一层上的后序结点，包含元素数据层
        self.forwards = [None] * (index_level + 1)


class Skiplist:
    def __init__(self, max_index_level=15):
        # 跳表初始化时指定跳表最大的索引层数，则跳表存储数据最大规模为2 ** (max_index_level + 1)
        self.max_index_level = max_index_level
        # 当前跳表的实际的索引最高层数
        self.list_index_level = 0
        self.head = Node(-1, max_index_level)

    def search(self, target: int) -> bool:
        head = self.head
        for i in range(self.list_index_level, -1, -1):
            while head.forwards[i] is not None and head.forwards[i].val < target:
                head = head.forwards[i]

        if head.forwards[0] is not None and head.forwards[0].val == target:
            return True
        return False

    def add(self, num: int) -> None:
        node_level = self.random_level(self.max_index_level)
        # list_index_level > node_level: 从当前最大索引层开始查找保证查找效率
        # node_level > list_index_level: 添加索引使用
        add_level = max(self.list_index_level, node_level)
        new_node = Node(num, node_level)

        head = self.head
        for i in range(add_level, -1, -1):
            while head.forwards[i] is not None and head.forwards[i].val < num:
                head = head.forwards[i]

            if i <= node_level:
                new_node.forwards[i] = head.forwards[i]
                head.forwards[i] = new_node
        self.list_index_level = add_level

    def erase(self, num: int) -> bool:
        head = self.head
        if_exist = False
        for i in range(self.list_index_level, -1, -1):
            while head.forwards[i] is not None and head.forwards[i].val < num:
                head = head.forwards[i]

            # 只删除一个值为num的结点
            if head.forwards[i] is not None and head.forwards[i].val == num:
            # 删除所有等于num的结点
            # while head.forwards[i] is not None and head.forwards[i].val == num:
                if_exist = True
                head.forwards[i] = head.forwards[i].forwards[i]

        # 更新list_index_level
        head = self.head
        for i in range(self.list_index_level, -1, -1):
            if head.forwards[i] is not None:
                self.list_index_level = i
                break

        return if_exist

    def random_level(self, max_level):
        level = 0
        while random.random() < 0.5 and level < max_level:
            level += 1

        return level

    def print_all(self):
        node = self.head.forwards[0]
        node_list = []
        while node:
            node_list.append('val: {}(index_level: {})'.format(node.val, node.index_level))
            node = node.forwards[0]

        print('=>'.join(node_list))


# if __name__ == "__main__":
#     sl = Skiplist()
#     sl.add(1)
#     sl.add(4)
#     sl.add(2)
#     sl.erase(0)
#     sl.add(3)
#     sl.add(3)
#     sl.add(3)
#     sl.erase(3)
#     sl.print_all()



# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)