# -*- coding: utf-8 -*-
# @Time    : 2022/4/6 15:28
# @Author  : MasterFive
# @FileName: check_in_clusion.py
# @Software: PyCharm


class Solution:
    def get_counts(self, s):
        counts = {}
        for i, c in enumerate(s):
            if c not in counts:
                counts[c] = 1
            else:
                counts[c] += 1
        return counts

    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts_1 = self.get_counts(s1)
        for i in range(len(s2) - len(s1) + 1):
            s = s2[i:i+len(s1)]
            counts_2 = self.get_counts(s)
            if counts_1 == counts_2:
                return True
        return False


if __name__ == '__main__':
    s1 = "adc"
    s2 = "dcda"  # true
    print(Solution().checkInclusion(s1, s2))

    s1 = "ab"
    s2 = "eidboaoo"  # false
    print(Solution().checkInclusion(s1, s2))
