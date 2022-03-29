# -*- coding: utf-8 -*-
# @Time    : 2022/3/29 17:56
# @Author  : MasterFive
# @FileName: first_bad_version.py
# @Software: PyCharm


def isBadVersion(version):
    return True


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        min_version = 1
        max_version = n
        while min_version <= max_version:
            version = (min_version + max_version) // 2
            is_bad_version = isBadVersion(version)
            if is_bad_version and not isBadVersion(version - 1):
                return version

            if not is_bad_version:
                min_version = version + 1
            else:
                max_version = version - 1

        return -1