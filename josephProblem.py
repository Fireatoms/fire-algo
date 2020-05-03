class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


def create_link_list(n):
    """不特意构造循环链表，而是直接使用函数生成循环链表"""

    head = Node(1)
    pre = head
    for i in range(2, n+1):
        new_node = Node(i)
        pre.next = new_node
        pre = new_node

    # 循环链表的尾结点指向头结点
    pre.next = head
    return head


def solve_joseph_problem(n, m):
    """返回最后的幸存者
    n: 一共n个人参与环形游戏
    m: 从当前位置算起，当前位置报数1，报数为m的被除名。然后从这个结点的下一个人开始从1报数，直到只剩下一个人
    这个就不存在最好，最坏，平均时间复杂度，根据循环逻辑，算法的时间复杂度稳稳的O(m*n)
    编号从1开始
    """
    head = create_link_list(n)
    if m == 1:
        # 此特殊情况代表按顺序从圈里将人除名
        print(n)
    else:
        pre = None
        cur = head
        # 幸存者会指向自己
        while cur.next != cur:
            for i in range(m-1):
                pre = cur
                cur = cur.next
            print("This man out: ", cur.value)
            pre.next = cur.next
            cur = pre.next

        print("Survival: ", cur.value)


def solve_joseph_array(n, m):
    """基于数组实现的约瑟夫问题解法
    非常适合训练下逻辑：整体循环比双向链表麻烦
    编号从0开始
    """
    cp = [1] * n
    num = 0
    out_count = 0 # 淘汰的人数
    # 循环条件的考虑和何时推出循环都要好好考量
    while out_count < n - 1:
        for i in range(n):
            if cp[i] == 1:
                num += 1
                if num == m:
                    print("out: ", i)
                    cp[i] = 0
                    num = 0
                    out_count += 1

            # 这个条件特别容易遗漏，导致内层for循环在outcount为n-1时没法按照预期退出
            if out_count == n - 1:
                break

    for i in range(n):
        if cp[i] == 1:
            print("survival: ", i)


def solve_joseph_recursion(n, m):
    """递归求解约瑟夫问题
    f(n,m) = (f(n-1,m) + m ) % n，这是编号从0开始的情况
    递推公式是如何推导得出的，还不明白,编号从1开始的递推公式也不清楚怎么写。
    """
    if n == 1:
        return 0
    else:
        return (solve_joseph_recursion(n-1, m) + m) % n


def solve_joseph_iteration(n, m):
    """将上面的递推公式转换成迭代循环来处理
    f(n,m) = (f(n-1,m) + m) % n
    """
    s = 0
    for i in range(2, n+1):
        s = (s+m) % i

    return s


if __name__ == '__main__':
    solve_joseph_problem(5, 2)
    # solve_joseph_array(5, 4)
    print(solve_joseph_recursion(5, 2))
    print(solve_joseph_iteration(5, 2))
