# link: https://leetcode-cn.com/problems/design-skiplist/
import random


class Node:
    def __init__(self, value):
        self.value = value
        # 0 => first linked list layer, 1 => first index layer
        self.max_index_level = 0
        # forwards[i] => the next node in ith layer
        self.forwards = []


class Skiplist:
    # This means skiplist has at most indexes of 15 layers except for the origin list layer.
    MAX_LIST_LEVEL = 15

    def __init__(self):
        # The largest index level of node except for the head node.
        self.index_level = 0
        self.head = Node(-1)
        self.head.max_index_level = self.MAX_LIST_LEVEL
        self.head.forwards = [None] * (self.MAX_LIST_LEVEL + 1)

    def search(self, target: int) -> bool:
        p = self.head
        for i in range(self.index_level, -1 ,-1):
            while p.forwards[i] is not None and p.forwards[i].value < target:
                p = p.forwards[i]

        if p.forwards[0] is not None and p.forwards[0].value == target:
            return True

        return False

    def add(self, num: int) -> None:
        index_level = self.random_level()
        new_node = Node(num)
        new_node.forwards = [None] * (index_level + 1)
        new_node.max_index_level = index_level
        new_max_level = max(self.index_level, index_level)

        p = self.head
        for i in range(new_max_level, -1, -1):
            while p.forwards[i] is not None and p.forwards[i].value < num:
                p = p.forwards[i]

            if i <= index_level:
                # insert index node
                new_node.forwards[i] = p.forwards[i]
                p.forwards[i] = new_node
        self.index_level = new_max_level

    def erase(self, num: int) -> bool:
        update = [None] * (self.index_level + 1)
        p = self.head

        for i in range(self.index_level, -1, -1):
            while p.forwards[i] is not None and p.forwards[i].value < num:
                p = p.forwards[i]
            update[i] = p

        if update[0].forwards[0] is not None and update[0].forwards[0].value == num:
            for i in range(self.index_level, -1, -1):
                if update[i].forwards[i] is not None and update[i].forwards[i].value == num:
                    update[i].forwards[i] = update[i].forwards[i].forwards[i]
            return True
        else:
            return False

    def random_level(self):
        level = 0
        # level in [0, 15]
        # probability： 1 / (2 ** (n + 1)).
        while random.random() < 0.5 and level < self.MAX_LIST_LEVEL:
            level += 1

        return level

    # def __repr__(self):
    #     message = []
    #     p = self.head.forwards[0]
    #     while p is not None:
    #         message.append('value: {}(index_level: {})'.format(str(p.value), p.max_index_level))
    #         p = p.forwards[0]
    #     return '->'.join(message)


# if __name__ == "__main__":
#     sl = Skiplist()
#     print(sl.add(1))
#     print(sl.add(2))
#     print(sl.add(3))
#     print(sl.search(0))
#     print(sl.add(4))
#     print(sl.search(1))
#     print(sl.erase(0))
#     print(sl.erase(1))
#     print(sl.search(1))


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)