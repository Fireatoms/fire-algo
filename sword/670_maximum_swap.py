# link: https://leetcode-cn.com/problems/maximum-swap/


class Solution:
    def maximumSwap(self, num: int):
        num_str = list(map(int, str(num)))
        bit_hash = {v: k for k, v in enumerate(num_str)}
        for idx, n in enumerate(num_str):
            for possible_num in range(9, n, -1):
                if bit_hash.get(possible_num, -1) > idx:
                    num_str[idx], num_str[bit_hash[possible_num]] = num_str[bit_hash[possible_num]], num_str[idx]
                    return int("".join(map(str,num_str)))
        return num


if __name__ == "__main__":
    sl = Solution()
    num = 19931227
    print(sl.maximumSwap(num))
