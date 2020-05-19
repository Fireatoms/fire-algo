# link: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/


class Solution:
    def numPairsDivisibleBy60(self, time) -> int:
        """brute solve
        不出意外，惨遭超时
        """
        pair_num = 0
        for i in range(len(time) - 1):
            # 注意循环起始点，j从i+1开始，而不是从i开始，从i开始会重复加和
            for j in range(i + 1, len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    pair_num += 1

        return pair_num

    def numPairsDivisibleBy60Hash(self, time) -> int:
        """
        公式求解参考：https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/discuss/256726/JavaPython-3-O(n)-code-w-comment-similar-to-Two-Sum
        核心点：找到求补公式：c = (60 - t % 60) % 60
        然后就是two sum问题了，利用hash表存储元素出现次数
        :param time:
        :return:
        """
        ch = {}
        pair_num = 0
        for i in time:
            c = (60 - i % 60) % 60
            pair_num += ch.get(c, 0)
            # ch[c] = ch.get(c, 0) + 1 又偷懒想当然了，这里怎么会是c
            ch[i % 60] = ch.get(i % 60, 0) + 1

        return pair_num


if __name__ == "__main__":
    time = [30,20,150,100,40]
    tc = Solution()
    tc.numPairsDivisibleBy60(time)