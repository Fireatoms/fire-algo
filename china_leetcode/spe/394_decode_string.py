# link: https://leetcode-cn.com/problems/decode-string/


class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multiple = [], '', 0

        for c in s:
            if c.isdigit():
                multiple = 10 * multiple + int(c)
            elif c == '[':
                stack.append((multiple, res))
                multiple, res = 0, ''
            elif c == ']':
                pre_multiple, pre_res = stack.pop()
                res = pre_res + pre_multiple * res
            else:
                res += c

        return res