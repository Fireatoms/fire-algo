# link: https://leetcode.com/problems/find-median-from-data-stream/
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.cap = 0

    def addNum(self, num: int) -> None:
        """insertion sort"""
        self.cap += 1
        self.data.append(num)

        # 插入排序不用range的原因：索引在跳出循环后还需要能够获取并进行相关操作
        # for i in range(self.cap - 2, -1, -1):
        #     if num < self.data[i]:
        #         self.data[i+1] = self.data[i]
        #     else:
        #         # 这个为何不写到这里的原因是，当插入的元素是插入后数组中最小元素时，0索引处应该放置num，但是这么写却无法实现
        #         # self.data[i+1] = num
        #         break
        i = self.cap - 2
        while i >= 0:
            if num < self.data[i]:
                self.data[i+1] = self.data[i]
            else:
                break
            i -= 1

        self.data[i+1] = num

    def findMedian(self) -> float:
        if self.cap % 2 == 0:
            return (self.data[self.cap//2 - 1] + self.data[self.cap//2]) / 2
        return self.data[self.cap//2]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


class MedianFinder1:
    """min_heap and max_heap"""

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.cap = 0
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        self.cap += 1
        if len(self.max_heap) == 0:
            # 堆结构的初始化，当大小顶堆中只有一个元素时，这个元素一定在大顶堆中，如果大顶堆长度为0说明整个数据结构中的元素个数为0
            heapq.heappush(self.max_heap, -num)
            return

        # 新元素插入操作
        if num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # 为了维持中位数的数据搬移操作
        if self.cap % 2 == 0:
            if len(self.max_heap) > self.cap//2:
                self.swap(self.max_heap, self.min_heap)
            elif len(self.max_heap) < self.cap//2:
                self.swap(self.min_heap, self.max_heap)
        else:
            if len(self.max_heap) > self.cap//2 + 1:
                self.swap(self.max_heap, self.min_heap)
            elif len(self.max_heap) < self.cap//2 + 1:
                self.swap(self.min_heap, self.max_heap)

    def swap(self, pop_heap, push_heap):
        val = heapq.heappop(pop_heap)
        heapq.heappush(push_heap, -val)


    def findMedian(self) -> float:
        if self.cap % 2 == 0:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        return -self.max_heap[0]


class MedianFinder1:
    """min_heap and max_heap"""

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # 无论num是否小于等于maxheap的堆顶，都先插入到大顶堆
        heapq.heappush(self.max_heap, -num)

        # 大顶推弹出堆顶到小顶堆（主要是处理大顶堆堆顶大于小顶堆堆顶的情况）
        # 这一步处理完成后，能够保证小顶堆中所有元素都大于等于大顶堆
        top_val = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, -top_val)

        # 无论奇数还是偶数，len(max_heap) >= len(min_heap)
        if len(self.max_heap) < len(self.min_heap):
            top_val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -top_val)

    def findMedian(self) -> float:
        # 这个返回函数写的是真蠢啊，max_heap的长度为奇数还是偶数根本不能决定整个堆中元素个数是偶数还是奇数
        # if len(self.max_heap) % 2 == 0:
        #     return (-self.max_heap[0] + self.min_heap[0]) / 2
        # return -self.max_heap[0]
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2

if __name__ == "__main__":
    mf = MedianFinder1()
    mf.addNum(1)
    mf.addNum(2)
    print(mf.findMedian())
    mf.addNum(3)
    print(mf.findMedian())