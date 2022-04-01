# -*- coding: utf-8 -*-
# @Time    : 2022/3/31 20:26
# @Author  : MasterFive
# @FileName: two_sum.py
# @Software: PyCharm
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        start, end = 0, n-1
        while start < end:
            num = numbers[start] + numbers[end]
            if num == target:
                return [start+1, end+1]
            if num > target:
                end -= 1
            else:
                start += 1
