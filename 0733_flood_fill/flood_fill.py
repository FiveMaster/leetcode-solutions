# -*- coding: utf-8 -*-
# @Time    : 2022/4/7 11:07
# @Author  : MasterFive
# @FileName: flood_fill.py
# @Software: PyCharm
from typing import List
import collections


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        origin_color = image[sr][sc]
        if origin_color == newColor:
            return image

        m, n = len(image), len(image[0])
        image[sr][sc] = newColor
        que = collections.deque([(sr, sc)])
        while que:
            x, y = que.popleft()
            for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= mx < m and 0 <= my < n and image[mx][my] == origin_color:
                    que.append((mx, my))
                    image[mx][my] = newColor
        return image
