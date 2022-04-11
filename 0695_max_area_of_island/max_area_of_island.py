# -*- coding: utf-8 -*-
# @Time    : 2022/4/7 11:32
# @Author  : MasterFive
# @FileName: max_area_of_island.py
# @Software: PyCharm
import collections
from typing import List


class Solution:
    def get_area_of_island(self, grid, sx, sy, passed_coors):
        area = 1
        passed_coors[(sx, sy)] = True
        m, n = len(grid), len(grid[0])
        que = collections.deque([(sx, sy)])
        while que:
            x, y = que.popleft()
            for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= mx < m and 0 <= my < n and grid[mx][my] == 1 and (mx, my) not in passed_coors:
                    passed_coors[(mx, my)] = True
                    area += 1
                    que.append((mx, my))

        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        passed_coors = {}
        max_area = 0
        for ax in range(len(grid)):
            for ay in range(len(grid[0])):
                if grid[ax][ay] == 0 or (ax, ay) in passed_coors:
                    continue

                island_area = self.get_area_of_island(grid, ax, ay, passed_coors)
                if max_area < island_area:
                    max_area = island_area
        return max_area


if __name__ == '__main__':
    grid = [[1]]

    print(Solution().maxAreaOfIsland(grid))