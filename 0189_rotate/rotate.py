# -*- coding: utf-8 -*-
# @Time    : 2022/3/30 18:16
# @Author  : MasterFive
# @FileName: rotate.py
# @Software: PyCharm
from typing import List


class Solution:
    def reverse_nums(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse_nums(nums, 0, len(nums) - 1)
        self.reverse_nums(nums, 0, k - 1)
        self.reverse_nums(nums, k, len(nums) - 1)

    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        result = nums.copy()
        for i in range(n):
            new_i = (i + k) % n
            nums[new_i] = result[i]

    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos_map = {}
        n = len(nums)
        for i in range(n):
            new_i = (i + k) % n
            pos_map[new_i] = nums[i]
        for i in range(n):
            nums[i] = pos_map[i]