# link: https://leetcode.com/problems/kth-largest-element-in-a-stream/
from typing import List
import heapq

# 自己实现堆数据结构
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # 在python中这个是引用，并不会增加实际的存储空间，同步修改
        self.data = nums
        self.k = k
        # 为了设置堆的边界条件，使用索引范围可以避免真实的删除数组元素带来的可能的数据搬移
        self.count = len(self.data)
        # 第一遍这里写了函数，但是居然没去调用，真的也是神奇了
        self.creat_k_little_heap()

    def creat_k_little_heap(self):
        for i in range(self.count//2 - 1, -1, -1):
            self.heapify(i)

        # 删除堆顶元素，直到堆中只有k的元素
        j = self.count - self.k
        for i in range(0, j):
            # 删除后堆的长度会减小一位
            self.data[0] = self.data[self.count-1]
            self.count -= 1
            self.heapify(0)

    def heapify(self, idx):
        """从上到下进行堆化"""
        while True:
            min_pos = idx
            if 2*idx+1 <= self.count - 1 and self.data[2*idx+1] < self.data[idx]:
                min_pos = 2*idx+1
            # 这里min_pos中间变量的引入蛮有技术含量的
            if 2*idx+2 <= self.count - 1 and self.data[2*idx+2] < self.data[min_pos]:
                min_pos = 2*idx+2
            if min_pos == idx:
                break
            self.data[idx], self.data[min_pos] = self.data[min_pos], self.data[idx]
            idx = min_pos

    def add(self, val: int) -> int:
        # 当k = len(num) + 1时，就有这个边界问题
        if self.count < self.k:
            self.data.append(val)
            self.count += 1
            i = self.count - 1
            while (i-1) // 2 >= 0 and self.data[i] < self.data[(i-1)//2]:
                self.data[i], self.data[(i-1)//2] = self.data[(i-1)//2], self.data[i]
                i = (i-1)//2
        else:
            if val > self.data[0]:
                self.data[0] = val
                self.heapify(0)

        return self.data[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


class KthLargest1:

    def __init__(self, k, nums):
        self.heap = nums
        self.k = k
        # python 内置函数处理list变为小顶堆
        heapq.heapify(self.heap)

        j = len(self.heap) - self.k
        while j > 0:
            heapq.heappop(self.heap)
            j -= 1

    def add(self, val):
        if self.k > len(self.heap):
            heapq.heappush(self.heap, val)
        else:
            if val > self.heap[0]:
                # 就这一个判断是否进行堆化就能优化很多时间消耗
                heapq.heapreplace(self.heap, val) # 92ms
            # heapq.heappushpop(self.heap, val) 156ms

        return self.heap[0]


if __name__ == "__main__":
    arr = [5, -1]
    k = 3
    kl = KthLargest1(k, arr)
    print(kl.add(2))
    print(kl.add(1))
    print(kl.add(-1))
    print(kl.add(3))
    print(kl.add(4))