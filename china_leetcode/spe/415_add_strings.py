# link: https://leetcode-cn.com/problems/add-strings/


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = []
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        while i >= 0 or j >= 0 or carry > 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            add_sum = n1 + n2 + carry
            carry = add_sum // 10
            ans.append(add_sum % 10)
            i -= 1
            j -= 1

        ans.reverse()
        return ''.join(map(str, ans))