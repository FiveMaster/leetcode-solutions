# -*- coding: utf-8 -*-
# @Time    : 2022/3/24 18:03
# @Author  : MasterFive
# @FileName: two_sum.py
# @Software: PyCharm
from typing import List


class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for x in range(length):
            for y in range(x + 1, length):
                if nums[x] + nums[y] == target:
                    return [x, y]


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for idx, x in enumerate(nums):
            nums_map[x] = idx
        for idx, x in enumerate(nums):
            if target - x in nums_map and nums_map[target - x] != idx:
                return [idx, nums_map[target - x]]


if __name__ == '__main__':
    print(Solution2().twoSum([2, 7, 11, 15], target=9))
    print(Solution2().twoSum([3, 2, 4], target=6))
    print(Solution2().twoSum([3, 3], target=6))
