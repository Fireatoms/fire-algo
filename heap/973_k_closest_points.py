# link: https://leetcode.com/problems/k-closest-points-to-origin/
from typing import List
import heapq
import random

class Solution:
    """用堆来实现
    耗时极长：3708 ms
    按理说建堆操作: O(n), k次出堆，每次时间消耗应该在lgn，klogn, 那么就应该是建堆比较耗时。总时间复杂度为o(n)
    """
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        """1. 建小顶堆 2. 顶部出堆k次"""
        l = len(points)
        res = []
        self.build_min_heap(points, l)
        for i in range(K):
            res.append(self.remove(points, l-i))

        return res

    def dist(self, points, i):
        """计算与原点距离，是元素出堆的凭证"""
        return points[i][0]**2 + points[i][1]**2

    def build_min_heap(self, arr, l):
        # 从0开始存储，第一个非叶子结点i//2 - 1
        idx = l//2 - 1
        while idx >= 0:
            # 注意啊：写了循环条件，结果循环里又不设置循环参考变量的变化，这不就死循环了吗
            self.heapify(arr, l, idx)
            idx -= 1

    def heapify(self, arr, l, idx):
        """l代表堆长度"""
        while True:
            min_pos = idx
            if 2*idx+1 < l and self.dist(arr, 2*idx+1) < self.dist(arr, idx):
                min_pos = 2*idx+1
            if 2*idx+2 < l and self.dist(arr, 2*idx+2) < self.dist(arr, min_pos):
                min_pos = 2*idx+2
            if min_pos == idx:
                break
            arr[idx], arr[min_pos] = arr[min_pos], arr[idx]
            # 随着值的交换，索引也要交换，使循环继续下去
            idx = min_pos

    def remove(self, arr, l):
        """我这里就不改变存储空间的大小，而是外部传参l来控制堆长度"""
        if l <= 0:
            return None
        val = arr[0]
        arr[0] = arr[l-1]
        self.heapify(arr, l-1, 0)
        return val

class Solution1:
    """直接使用python自带的排序算法进行排序
    时间消耗：864 ms，见了鬼了，比我的堆排序还要快
    """
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda x: x[0]**2 + x[1]**2)
        return points[:K]

class Solution2:
    """直接使用python自带的堆排序进行处理
    时间消耗：960 ms 耗时也是和直接排序的不相上下
    """
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return heapq.nsmallest(K, points, key=lambda x: x[0]**2 + x[1]**2)

class Solution3:
    """直接使用python自带的堆排序进行处理
    时间消耗：1016 ms 耗时也是和直接排序的不相上下, 也出现过720ms，这个量级基本是一致，细微差别是lc服务器运算能力问题
    也比我的操作快，研究下heap包是怎么做的
    """
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # 这里的思路是先堆化，然后remove出去，区别仅仅是建堆和出堆的操作调用的是python的包函数
        res = []
        distances = [(point[0]**2 + point[1]**2, point[0], point[1]) for point in points]
        heapq.heapify(distances)

        for i in range(min(K, len(points))):
            item = heapq.heappop(distances)
            res.append(item[1:])

        return res

class Solution4:
    """前k大，这个可以使用快排的partition函数进行操作
    时间消耗：936 ms 比我用堆写的还快
    """
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        self.quick_sort(points, 0, len(points)-1, K)
        return points[:K]

    def quick_sort(self, arr, p, r, k):
        pivot = random.randint(p, r)
        arr[pivot], arr[r] = arr[r], arr[pivot]
        q = self.partition(arr, p, r)
        if q > k - 1:
            self.quick_sort(arr, p, q-1, k)
        elif q < k - 1:
            self.quick_sort(arr, q+1, r, k)
        else:
            return

    def dist(self, points, i):
        return points[i][0]**2 + points[i][1]**2

    def partition(self, arr, p, r):
        i = j = p
        pivot_dist = self.dist(arr, r)
        while j < r:
            if self.dist(arr, j) < pivot_dist:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
            j += 1

        arr[i], arr[r] = arr[r], arr[i]
        return i


if __name__ == "__main__":
    points = [[3, 3], [5, -1], [-2, 4]]
    K = 2
    sl = Solution4()
    print(sl.kClosest(points, K))
