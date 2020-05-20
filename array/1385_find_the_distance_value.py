# link: https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

class Solution:
    def findTheDistanceValue(self, arr1, arr2, d: int) -> int:
        """这是一道题意非常魔幻的题目，随便搞一下也罢"""
        dis = 0
        for i in range(len(arr1)):
            flag = True
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    flag = False
                    break

            if flag:
                dis += 1
        return dis


if __name__ == "__main__":
    arr1 = [4, 5, 8]
    arr2 = [10, 9, 1, 8]
    d = 2
    sc = Solution()
    v = sc.findTheDistanceValue(arr1, arr2, d)
    print(v)