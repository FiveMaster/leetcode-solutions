# -*- coding: utf-8 -*-
# @Time    : 2022/3/28 18:32
# @Author  : MasterFive
# @FileName: length_of_longest_substring.py
# @Software: PyCharm
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        substring = {}
        max_len = 0
        min_idx = max_idx = 0
        for idx, a in enumerate(s):
            if a in substring:
                if (max_idx - min_idx + 1) > max_len:
                    max_len = (max_idx - min_idx + 1)
                if min_idx < substring[a] + 1:
                    min_idx = substring[a] + 1
            max_idx = idx
            substring[a] = idx
        return (max_idx - min_idx + 1) if (max_idx - min_idx + 1) > max_len else max_len


if __name__ == '__main__':
    s = "abba"  # 2
    print(Solution().lengthOfLongestSubstring(s))

    s = "abcabcbb"  # 3
    print(Solution().lengthOfLongestSubstring(s))

    s = "pwwkew"  # 3
    print(Solution().lengthOfLongestSubstring(s))

    s = "bbbbb"  # 1
    print(Solution().lengthOfLongestSubstring(s))

    s = "dvdf"  # 3
    print(Solution().lengthOfLongestSubstring(s))

    s = " "  # 1
    print(Solution().lengthOfLongestSubstring(s))