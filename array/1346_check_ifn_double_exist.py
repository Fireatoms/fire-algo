class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        """时间复杂度o(n)，空间复杂度o(n)，本质上是空间换时间，引入hashset来简化查找操作（in判断是o(1)时间复杂度）"""
        arr_set = set()
        for i in arr:
            if 2 * i in arr_set or i % 2 == 0 and i // 2 in arr_set:
                return True
            arr_set.add(i)

        return False