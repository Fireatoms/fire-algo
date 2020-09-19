# link: https://leetcode.com/problems/ransom-note/
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_note_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        for k, v in ransom_note_count.items():
            if k not in magazine_count or v > magazine_count[k]:
                return False

        return True