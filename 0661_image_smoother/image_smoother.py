# -*- coding: utf-8 -*-
# @Time    : 2022/3/24 17:18
# @Author  : MasterFive
# @FileName: image_smoother.py
# @Software: PyCharm
from typing import List


class Solution:
    def get_coordinates(self, x, y):
        coordinates = [(x, y),
                       (x, y - 1),
                       (x + 1, y),
                       (x, y + 1),
                       (x - 1, y),
                       (x - 1, y - 1),
                       (x + 1, y - 1),
                       (x + 1, y + 1),
                       (x - 1, y + 1)]
        return coordinates

    def cal_value(self, coordinates, img):
        m, n = len(img), len(img[0])
        total_value = 0
        total_count = 0
        for x, y in coordinates:
            if 0 <= x < m and 0 <= y < n:
                total_value += img[x][y]
                total_count += 1
        return total_value // total_count

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        new_img = []
        for x in range(len(img)):
            row = []
            for y in range(len(img[0])):
                row.append(self.cal_value(self.get_coordinates(x, y), img))
            new_img.append(row)
        return new_img


img = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
print(Solution().imageSmoother(img))
