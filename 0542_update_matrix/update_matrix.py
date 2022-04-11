# -*- coding: utf-8 -*-
# @Time    : 2022/4/7 18:02
# @Author  : MasterFive
# @FileName: update_matrix.py
# @Software: PyCharm
from typing import List
import collections


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        coor_0 = []
        m, n = len(mat), len(mat[0])
        for x in range(m):
            for y in range(n):
                if mat[x][y] == 0:
                    coor_0.append((x, y))
        result = [[0]*n for i in range(m)]
        que = collections.deque(coor_0)
        seen = set(coor_0)

        while que:
            i, j = que.popleft()
            for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0<=ni<m and 0<=nj<n and (ni, nj) not in seen:
                    result[ni][nj] = result[i][j] + 1
                    que.append((ni, nj))
                    seen.add((ni, nj))
        return result
