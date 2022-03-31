# -*- coding: utf-8 -*-
# @Time    : 2022/3/31 11:17
# @Author  : MasterFive
# @FileName: move_zeroes.py
# @Software: PyCharm
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p, q = 0, 0
        while q < n:
            if nums[q] != 0:
                nums[p], nums[q] = nums[q], nums[p]
                p += 1
            q += 1


if __name__ == '__main__':
    t_nums = [0, 1, 0, 3, 12]  # [1,3,12,0,0]
    Solution().moveZeroes(t_nums)
    print(t_nums)

    t_nums = [0]  # [0]
    Solution().moveZeroes(t_nums)
    print(t_nums)

