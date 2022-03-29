# -*- coding: utf-8 -*-
# @Time    : 2022/3/29 17:44
# @Author  : MasterFive
# @FileName: search.py
# @Software: PyCharm
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
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

        return -1


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9  # 4
    print(Solution().search(nums, target))

    nums = [-1,0,3,5,9,12]
    target = 2  # 4
    print(Solution().search(nums, target))
