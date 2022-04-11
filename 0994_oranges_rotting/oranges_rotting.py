# -*- coding: utf-8 -*-
# @Time    : 2022/4/8 10:44
# @Author  : MasterFive
# @FileName: oranges_rotting.py
# @Software: PyCharm
from typing import List
import collections


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        bad_pos = []
        m, n = len(grid), len(grid[0])
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 2:
                    bad_pos.append((x, y, 0))
        que = collections.deque(bad_pos)
        d = 0
        while que:
            i, j, d = que.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    que.append((ni, nj, d + 1))
        if any(1 in row for row in grid):
            return -1

        return d
