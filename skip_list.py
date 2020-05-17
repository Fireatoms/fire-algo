# 跳表：带索引的链表，简化起见，存的是正整数，且数据不重复
import random


class Node:
    """跳表结点数据结构
    1. value：存储的数据值（索引也沿用这个值）
    2. forwards: 数组，存放结点的后序结点（含原始数据层与索引层）
    3. 原始数据层：没加任何索引的原始链表存储结构
    4. 索引层：假如此结点有2级索引，那么forwards数据的0，1，2索引分别代表原始数据层，第一层，第二层的前序结点
    """
    def __init__(self, value):
        self.value = value
        self.forwards = []
        # 记录下当前结点有多少级索引（含原始数据层，所以1实际代表没加索引），对算法实现没有意义，仅作为记录使用
        self.max_index_level = 1


class SkipList:
    # 此跳表最多16级索引，n/2^16 = 2，每2个结点抽出一个索引，按照这个规则可以推算下原始链表中的数据为2^17个，logn的时间复杂度实在是高效
    MAX_LEVEL = 16

    def __init__(self):
        # 跳表的高度，高度为1代表未加索引，为了查询的便利，要从最高层索引开始查找才能保证logn的高效率
        self.index_level = 1
        self.head = Node(-1)
        self.head.forwards = [None] * self.MAX_LEVEL

    def insert(self, value):
        """插入应该从当前的最大索引层开始找，而不是从新增的结点的最大索引层开始找，下面写个优化方法"""
        level = self.random_level()
        # 初始化新结点
        new_node = Node(value)
        new_node.max_index_level = level
        # 初始化索引层，level为1时，代表无索引，只需要把结点插入到0层的原始数据层即可
        new_node.forwards = [None] * level
        # 记录结点插入的前序位置
        update = [None] * level
        p = self.head
        for i in range(level - 1, -1, -1):
            # 这里p从上层遍历查找，然后下层起点是上层循环终止时的p。这样对应到跳表的查找逻辑上，logn的时间复杂度就全对上了
            while p.forwards[i]  and p.forwards[i].value < value:
                p = p.forwards[i]

            update[i] = p

        for i in range(level -  1, -1, -1):
            new_node.forwards[i] = update[i].forwards[i]
            update[i].forwards[i] = new_node

        # 更新跳表的索引层数
        if level > self.index_level:
            self.index_level = level

    def efficient_insert(self, value):
        level = self.random_level()
        new_node = Node(value)
        new_node.max_index_level = level
        new_node.forwards = [None] * level
        # max_level：开始搜索位置的最大索引层数。两种情况：1. 新插入结点level大于当前跳表的索引层数 2. 新插入结点level小于当前跳表索引层数
        # 1情况时，从level开始建立索引，并且插入成功后更新跳表的索引层数到level
        # 2情况时，从跳表index_level索引层数开始为了能够尽快的找到待插入位置
        max_level = max(level, self.index_level)
        update = [None] * level

        p = self.head
        for i in range(max_level - 1, -1, -1):
            while p.forwards[i] and p.forwards[i].value < value:
                p = p.forwards[i]

            if i < level:
                update[i] = p

        for i in range(level - 1, -1, -1):
            new_node.forwards[i] = update[i].forwards[i]
            update[i].forwards[i] = new_node

        self.index_level = max_level

    def find(self, value):
        p = self.head
        for i in range(self.index_level - 1, -1, -1):
            while p.forwards[i] and p.forwards[i].value < value:
                p = p.forwards[i]

        if p.forwards[0] and p.forwards[0].value == value:
            return p.forwards[0]
        else:
            return None

    def delete(self, value):
        p = self.head
        # 存放每一层索引上待删除结点的可能前序结点
        update = [None] * self.index_level
        for i in range(self.index_level - 1, -1, -1):
            # forward[i]为None或者forward[i].value >= value时循环退出
            while p.forwards[i] and p.forwards[i].value < value:
                p = p.forwards[i]

            update[i] = p

        # 第一遍直接写了这个循环也没错，但是先判断一下value是否在跳表中能够避免很多不必要的循环比较工作
        if p.forwards[0] and p.forwards[0].value == value:
            for i in range(self.index_level - 1, -1, -1):
                if update[i] and update[i].value == value:
                    update[i].forwards[i] = update[i].forwards[i].forwards[i]

    def random_level(self):
        """
        没有索引，只在原始数据层有结点，则此时level为1
        随机生成索引层数，2-15层，按照数量的比例为0.5 0.25...,这里设置的索引层数的随机函数选择0.5比较正是处于这个概率的考虑
        :return:
        """
        level = 1
        # 注意看这里的循环退出条件，不是一定要循环MAX_LEVEL次，如果是固定循环次数的话，这就变成组合数的概率了，不是上面要的成比例的概率分布
        while random.random() < 0.5 and level < self.MAX_LEVEL:
            level += 1

        return level

    def __repr__(self):
        message = []
        p = self.head
        while p.forwards[0]:
            message.append('value: ' + str(p.forwards[0].value) + '(index_level: ' +
                           str(p.forwards[0].max_index_level) + ')')
            p = p.forwards[0]
        return '->'.join(message)


def test_skip_list():
    sl = SkipList()
    for i in range(10):
        sl.efficient_insert(i)
    print(sl)


if __name__ == "__main__":
    test_skip_list()
