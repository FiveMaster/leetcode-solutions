# -*- coding: utf-8 -*-
# @Time    : 2022/3/30 18:04
# @Author  : MasterFive
# @FileName: sorted_squres.py
# @Software: PyCharm
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        p, q, pos = 0, n - 1, n - 1
        while p <= q:
            if nums[p] * nums[p] > nums[q] * nums[q]:
                result[pos] = nums[p] * nums[p]
                p += 1
            else:
                result[pos] = nums[q] * nums[q]
                q -= 1
            pos -= 1
        return result


if __name__ == '__main__':
    nums = [-4,-1,0,3,10]  # [0,1,9,16,100]
    print(Solution().sortedSquares(nums))

    nums = [-7,-3,2,3,11]  # [4,9,9,49,121]
    print(Solution().sortedSquares(nums))