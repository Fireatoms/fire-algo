class MergeHeap:
    """小顶堆"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        # 要带脑子，0索引无用，从1开始用的
        self.data = [None] * (capacity+1)

    def insert(self, value):
        """value格式举例：10-9，前面的10是真正用于比较的数值，后面的9是数据流的编号"""
        # 延续惯例，从索引位置1开始存放数据，i索引的左子结点：2*i，右子结点：2*i+1，父结点：i//2
        if self.count >= self.capacity:
            return

        self.count += 1
        self.data[self.count] = value
        i = self.count
        while i//2 > 0 and self.large_than(self.data[i//2], self.data[i]):
            self.swap(i, i//2)
            i = i // 2

    def remove_root(self):
        if self.count <= 0:
            return None, None

        root = self.data[1]
        self.data[1] = self.data[self.count]
        self.count -= 1
        self.heapify(1)
        root_val, root_stream_num = self.parse_value(root)
        return root_val, root_stream_num

    def heapify(self, idx):
        """将某个结点从上到下进行堆化"""
        while True:
            # 从处理完成后的结果来判断是否发生了父子结点的交换，如果没有，则无需继续往下堆化，循环堆化可以停止
            min_pos = idx
            if 2*idx <= self.count and self.large_than(self.data[idx], self.data[2*idx]):
                min_pos = 2*idx
            if 2*idx+1 <= self.count and self.large_than(self.data[min_pos], self.data[2*idx+1]):
                min_pos = 2*idx+1
            if idx == min_pos:
                break
            self.swap(idx, min_pos)
            idx = min_pos

    def swap(self, p_inx, q_inx):
        self.data[p_inx], self.data[q_inx] = self.data[q_inx], self.data[p_inx]

    def large_than(self, pre, post):
        """前面的参数大于等于后面参数时，返回true，否则返回false"""
        pre_heap_val, pre_stream_num = self.parse_value(pre)
        post_heap_val, post_stream_num = self.parse_value(post)
        return pre_heap_val > post_heap_val

    def parse_value(self, val):
        sep_index = val.index('-')
        return int(val[0:sep_index]), int(val[sep_index+1:])

    def is_empty(self):
        return self.count == 0