# -*- coding: utf-8 -*-
# @Time    : 2022/3/29 18:06
# @Author  : MasterFive
# @FileName: search_insert.py
# @Software: PyCharm
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        min_index = 0
        max_index = len(nums) - 1
        while min_index <= max_index:
            index = (min_index + max_index) // 2
            if nums[index] == target:
                return index

            if nums[index] < target:
                min_index = index + 1
            else:
                max_index = index - 1

        return (min_index + max_index) // 2 + 1


Solution().searchInsert([1, 3, 5, 6], 2)