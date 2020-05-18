class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        k_arr = []
        add_arr = []
        while K > 0:
            k_bit = K % 10
            K = K // 10
            k_arr.append(k_bit)

        k_arr.reverse()
        a_index = len(A) - 1
        k_index = len(k_arr) - 1
        carry_set = 0
        while a_index >= 0 and k_index >= 0:
            b_sum = A[a_index] + k_arr[k_index] + carry_set
            add_bit = b_sum % 10
            carry_set = b_sum // 10
            add_arr.append(add_bit)
            a_index -= 1
            k_index -= 1

        while a_index >= 0:
            b_sum = A[a_index] + carry_set
            add_bit = b_sum % 10
            carry_set = b_sum // 10
            add_arr.append(add_bit)
            a_index -= 1

        while k_index >= 0:
            b_sum = k_arr[k_index] + carry_set
            add_bit = b_sum % 10
            carry_set = b_sum // 10
            add_arr.append(add_bit)
            k_index -= 1

        if carry_set != 0:
            add_arr.append(carry_set)

        add_arr.reverse()
        return add_arr

    def addToArrayFormSimplify(self, A: List[int], K: int) -> List[int]:
        """
        因为题目限定了K的范围，所以不需要像上面解法那样将K按为拆解，直接将K加到A数组的最后一位即可
        用一个数组记录加和，终止条件是进位为0且A数组倒序遍历完成
        :param A:
        :param K:
        :return:
        """
        add_arr = []
        a_index = len(A) - 1
        carry = K
        # 循环条件一定要想清楚，有没有=其实都是要对应到实际过程的，一定不能糊弄过去
        while carry > 0 or a_index >= 0:
            if a_index >= 0:
                carry = carry + A[a_index]

            add_arr.append(carry % 10)
            carry //= 10
            # 写python循环的时候特别容易忘记循环参数的变化
            a_index -= 1

        add_arr.reverse()

        return add_arr



