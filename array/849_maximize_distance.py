# link: https://leetcode.com/problems/maximize-distance-to-closest-person/
import itertools


class Solution:
    def maxDistToClosest(self, seats):
        """left代表某个位置到左手边的最大距离
        right代表某个位置到右手边最大距离
        max_i = min(left[i], right[i])
        max = max(max_0 .. max_n)
        """
        n = len(seats)
        left = [n] * n
        right = [n] * n

        # 数值是从某个点到最近的1的距离。0 0 1 0，这种left[0] = inf, left[1] = inf。这里为了算法实现简便，干脆设置left[0] = n
        # 这个n值是人员总数，针对min(left[i], right[i])的逻辑来看相当于inf
        # left求解时最左不处理，right求解时最右不处理
        # 错了，这样漏掉了最左或最右为1的情况
        # for i in range(1, n):
        #     if seats[i] == 1:
        #         # 1是相对位置标杆,初始化标杆的意味
        #         left[i] = 0
        #     else:
        #         left[i] = left[i-1] + 1
        #
        # for i in range(n-2, -1, -1):
        #     if seats[i] == 1:
        #         right[i] = 0
        #     else:
        #         right[i] = right[i+1] + 1
        for i in range(n):
            if seats[i] == 1:
                left[i] = 0
            elif i > 0:
                left[i] = left[i-1] + 1

        for i in range(n-1, -1, -1):
            if seats[i] == 1:
                right[i] = 0
            elif i < n -1:
                right[i] = right[i+1] + 1

        ans = 0
        for i in range(n):
            ans = max(ans, min(left[i], right[i]))

        return ans

    def maxDistToClosest(self, seats):
        """双指针来做计算，pre，fur
        i位置左边为pre，右边为fur，min(i-pre, fur-i)代表当前位置最近的人的距离
        pre < i < fur。这里我用-1代表最左端无人，用n代表最右端无人
        逻辑就是计算每个值为0的位置的到最近人的距离，
        """
        n = len(seats)
        pre = -1
        fur = 0
        ans = 0 # 记录结果
        for i, v in enumerate(seats):
            if v == 1:
                pre = i
            else:
                while fur < i or (fur < n and seats[fur] == 0):
                    fur += 1

                left = n if pre == -1 else i - pre
                right = n if fur == n else fur - i
                ans = max(ans, min(left, right))

        return ans


    def maxDistToClosest(self, seats):
        """使用python的生成器逐个生成fur值
        -1代表最左端无人，n代表最右端无人
        """
        n = len(seats)
        pre = -1
        fur_gen = (i for i, seat in enumerate(seats) if seat)
        fur = next(fur_gen)

        ans = 0
        for i, v in enumerate(seats):
            if v == 1:
                pre = i
            else:
                while fur != n and fur < i:
                    fur = next(fur_gen, n)

                left = n if pre == -1 else i - pre
                right = n if fur == n else fur - i

                ans = max(ans, min(left, right))

        return ans

    def maxDistToClosest(self, seats):
        """与上面生成器的解决思路一致
        目的：训练模拟生成器的概念，用数组实现
        """
        n = len(seats)
        pre = -1
        fur_arr = []
        for i, v in enumerate(seats):
            if v == 1:
                fur_arr.append(i)
        # 当最右端没有1时用n代表无穷大
        fur_arr.append(n)
        fur = fur_arr[0]
        nfi = 0

        ans = 0
        for i, v in enumerate(seats):
            if v == 1:
                pre = i
            else:
                while fur < i and fur != n:
                    nfi += 1
                    fur = fur_arr[nfi]

                left = n if pre == -1 else i - pre
                right = n if fur == n else fur - i
                ans = max(ans, min(left, right))

        return ans

    def maxDistToClosest(self, seats):
        """python like
        基本思想是1 0 0 0 1这种中间有k（3）个位置的情况，中间位置的最大相邻距离为 （k+1）/2 - 1 + 1
        why：找出中间值（k+1）/2, 然后1-k的索引下，中间值减去1，由于两边还有1，距离需要再加1.最终值为（k+1）/2，并且这个值要舍掉小数
        注意这样两种特殊情况：0 0 1 和 0 0 1，这两种情况下上面k分组根据组长计算的公司不成立。直接取1的index
        深度使用python中语法的意义：提升开发速度（应该也要关注下python内置函数的效率），因为实际开发过程中，并不一定要求极致效率（并且
        内置函数比自己实现效率可能还要更高）。成为语言下的熟练工。
        但也要再用一般思想实现一遍，毕竟很多没有特别高级函数的语言需要你能自己开发
        """
        ans = 0
        for seat, group in itertools.groupby(seats):
            if not seat:
                k = len(list(group))
                ans = max(ans, (k+1)/2)

        return max(ans, seats.index(1), seats[::-1].index(1))

    def maxDistToClosest(self, seats):
        """使用基本的数据结构和逻辑"""
        n = len(seats)
        ans = 0
        k = 0
        for i, v in enumerate(seats):
            if v == 1:
                ans = max(ans, int((k + 1) / 2))
                k = 0
            else:
                k += 1

        for i in range(n):
            if seats[i] == 1:
                ans = max(ans, i)
                break

        for i in range(n-1, -1, -1):
            if seats[i] == 1:
                ans = max(ans, n-1-i)
                break

        return ans
