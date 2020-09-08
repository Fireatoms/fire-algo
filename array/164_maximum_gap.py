# link: https://leetcode.com/problems/maximum-gap/
from typing import List


class Solution:
    def maximumGapSort(self, nums: List[int]) -> int:
        nums.sort()
        max_gap = 0
        for i in range(len(nums)-1):
            max_gap = max(max_gap, nums[i+1] - nums[i])
        return max_gap

    def maximumGapBucket(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        n = len(nums)
        num_max = max(nums)
        num_min = min(nums)
        interval = max(1, (num_max - num_min) // (n - 1))

        bucket_num = (num_max - num_min) // interval + 1
        buckets = [None] * bucket_num

        for num in nums:
            bucket_idx = (num - num_min) // interval
            if not buckets[bucket_idx]:
                buckets[bucket_idx] = {'min': num, 'max': num}
            else:
                buckets[bucket_idx]['min'] = min(buckets[bucket_idx]['min'], num)
                buckets[bucket_idx]['max'] = max(buckets[bucket_idx]['max'], num)

        pre_max, max_gap = num_min, 0
        for bucket in buckets:
            if bucket:
                max_gap = max(max_gap, bucket['min'] - pre_max)
                pre_max = bucket['max']

        return max_gap


if __name__ == "__main__":
    arr = [3, 6, 9, 1]
    sl = Solution()
    print(sl.maximumGapBucket(arr))