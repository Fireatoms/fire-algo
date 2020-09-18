# link: https://leetcode.com/problems/russian-doll-envelopes/


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        assend_list = []
        for envelope in envelopes:
            if not assend_list or envelope[-1] > assend_list[-1]:
                assend_list.append(envelope[-1])
            else:
                pos, low, high = 0, 0, len(assend_list) - 1
                while low <= high:
                    # There must exist more than an element in assend_list which is larger than the target,
                    # beause envelope[-1] <= assend_list[-1]
                    mid = low + (high - low) // 2
                    if assend_list[mid] >= envelope[-1]:
                        if mid == 0 or assend_list[mid - 1] < envelope[-1]:
                            pos = mid
                            break
                        else:
                            high = mid - 1
                    else:
                        low = mid + 1

                assend_list[pos] = envelope[-1]

        return len(assend_list)