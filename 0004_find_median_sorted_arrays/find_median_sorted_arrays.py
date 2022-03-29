# -*- coding: utf-8 -*-
# @Time    : 2022/3/29 15:46
# @Author  : MasterFive
# @FileName: find_median_sorted_arrays.py
# @Software: PyCharm
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0 and len(nums2) == 0:
            return 0.0

        if len(nums1) == 0:
            return (nums2[len(nums2) // 2 - 1] + nums2[len(nums2) // 2]) / 2 if (len(nums2) % 2) == 0 else nums2[len(nums2) // 2]

        if len(nums2) == 0:
            return (nums1[len(nums1) // 2 - 1] + nums1[len(nums1) // 2]) / 2 if (len(nums1) % 2) == 0 else nums1[len(nums1) // 2]

        mid_value_min = 0
        mid_value_max = 0
        index1 = index2 = 0
        for i in range((len(nums1) + len(nums2)) // 2 + 1):
            mid_value_min = mid_value_max
            if index1 < len(nums1) and index2 < len(nums2):
                if nums1[index1] <= nums2[index2]:
                    mid_value_max = nums1[index1]
                    index1 += 1
                else:
                    mid_value_max = nums2[index2]
                    index2 += 1
            elif index1 < len(nums1):
                mid_value_max = nums1[index1]
                index1 += 1
            else:
                mid_value_max = nums2[index2]
                index2 += 1
        return float((mid_value_min + mid_value_max) / 2.0 if (len(nums1) + len(nums2)) % 2 == 0 else mid_value_max)


if __name__ == '__main__':
    nums1 = [2, 2, 4, 4]
    nums2 = [2, 2, 4, 4]  # 3.0000
    print(Solution().findMedianSortedArrays(nums1, nums2))

    nums1 = []
    nums2 = [2, 3]  # 2.5000
    print(Solution().findMedianSortedArrays(nums1, nums2))

    nums1 = []
    nums2 = [1]  # 1.0000
    print(Solution().findMedianSortedArrays(nums1, nums2))

    nums1 = [1,3]
    nums2 = [2]  # 2.00000
    print(Solution().findMedianSortedArrays(nums1, nums2))

    nums1 = [1, 2]
    nums2 = [3, 4]  # 2.50000
    print(Solution().findMedianSortedArrays(nums1, nums2))

