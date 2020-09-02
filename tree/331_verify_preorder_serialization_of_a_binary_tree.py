# link: https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
# solution: https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/discuss/78588/Python-solution-with-detailed-explanation

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        pre_list = preorder.split(',')
        stack = []
        for s in pre_list:
            stack.append(s)
            while len(stack) > 2 and stack[-2] == '#' and stack[-1] == '#':
                stack.pop()
                stack.pop()
                if stack.pop() == '#':
                    return False
                stack.append('#')

        return len(stack) == 1 and stack[-1] == '#'