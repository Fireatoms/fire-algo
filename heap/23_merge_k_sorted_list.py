from typing import List
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    时间复杂度nk，当k比较大时我这个超时了，我现在只能想到一种解释，就是我的单次操作耗时较长
    具体是哪里超时严重，暂时没搞明白
    问题还是出在这个k值上面，当k与n大小相近时，这个时间复杂度为n2
    下面的暴力求解时间复杂度在nlogn，这种情况下反而时间复杂度更优
    """
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode()
        p = head
        if lists:
            while True:
                min_pos = 0
                for i in range(len(lists)):
                    if lists[min_pos] is None and lists[i]:
                        min_pos = i

                    if lists[i] and lists[i].val < lists[min_pos].val:
                        min_pos = i

                if lists[min_pos]:
                    p.next = lists[min_pos]
                    p = p.next
                    lists[min_pos] = lists[min_pos].next
                else:
                    break

        return head.next


class Solution1:
    """
    思路极为简单，遍历得到所有结点值组成的数组，然后对数组进行排序，再用已排序的数组值构造新的链表
    空间复杂度会是o(n)，排序是最耗时的操作，利用语言自带的排序，一般时间复杂度可以做到稳定的o(nlogn)
    我还蛮喜欢这个暴力求解的，足够简单明了，除了空间复杂度比较高外，时间复杂度在可接收的范围，比上面的k*n好，因为k是不可控的，一旦k值与n值
    相近，这个时间复杂度就飙升。
    """
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        val_list = []
        for l in lists:
            while l:
                val_list.append(l.val)
                l = l.next

        head = p = ListNode()
        val_list.sort()
        for v in val_list:
            p.next = ListNode(v)
            p = p.next

        return head.next


class Solution2:
    """
    维护小顶堆，不断的出堆更新链表，同时不断的将新元素入堆。重复这两个过程。
    用小顶堆实现，但是要注意的是堆化的时候的大小比较原则，heapq没法直接比较两个node类型，想要用node.val来做比较可以构造元组来实现，
    (node.val, node)，但是这里也还是有个问题，val值重复时，heapq会默认选用元组中第二个元素进行比较，那么此时会报错。
    这里有两个解决方案：
    1. (node.val, id(node), node)：不同对象的内存地址不会重复
    2. (lists[idx].val, idx)：针对这个题目，直接用lists数组的索引来取具体的结点，利用上lists索引的唯一性做比较更加巧妙。
    比较下1实际上实现更加简单，堆建立完成后无需再更新原lists元素，但是2因为使用了lists的索引来寻找元素，所以每次操作后还需要更新lists中
    元素的状态。
    """
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 只需要将非None元素放入初始化的堆中
        heap_list = [(lists[i].val, i) for i in range(len(lists)) if lists[i]]
        heapq.heapify(heap_list)

        head = p = ListNode()
        while heap_list:
            # 出堆，更新结果链表
            heap_item = heapq.heappop(heap_list)
            node = ListNode(heap_item[0])
            p.next = node
            p = p.next

            # 将新的元素入堆
            if lists[heap_item[1]].next:
                lists[heap_item[1]] = lists[heap_item[1]].next
                heapq.heappush(heap_list, (lists[heap_item[1]].val, heap_item[1]))

        return head.next


def construct_k_sorted_list():
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    l3 = ListNode(2)
    l3.next = ListNode(6)

    return [l1, l2, l3]


if __name__ == "__main__":
    lists = construct_k_sorted_list()
    sl = Solution()
    res = sl.mergeKLists(lists)
    print('done')