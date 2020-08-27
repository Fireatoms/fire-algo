# link: https://leetcode.com/problems/path-sum-ii/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return None

        res = []
        self.dfs(root, 0, '', res, sum)
        return res

    def dfs(self, root, sum_res, path_record, res, sum):
        if not root.left and not root.right:
            sum_res += root.val
            if sum_res == sum:
                path_arr_str = (path_record+str(root.val)).split(',')
                path_arr_int = list(map(int, path_arr_str))
                res.append(path_arr_int)
        if root.left:
            self.dfs(root.left, sum_res+root.val, path_record+str(root.val)+',', res, sum)
        if root.right:
            self.dfs(root.right, sum_res+root.val, path_record+str(root.val)+',', res, sum)


class SolutionList:
    def pathSum(self, root, sum):
        if not root:
            return None

        res = []
        self.dfs(root, 0, [], res, sum)
        return res

    def dfs(self, root, sum_res, path_list, res, sum):
        if not root.left and not root.right:
            sum_res += root.val
            if sum_res == sum:
                res.append(path_list + [root.val])
        if root.left:
            self.dfs(root.left, sum_res+root.val, path_list+[root.val], res, sum)
        if root.right:
            self.dfs(root.right, sum_res + root.val, path_list + [root.val], res, sum)