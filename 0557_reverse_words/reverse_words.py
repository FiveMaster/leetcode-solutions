# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 14:21
# @Author  : MasterFive
# @FileName: reverse_words.py
# @Software: PyCharm



class Solution:
    def reverse_string(self, s):
        start, end = 0, len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return "".join(s)

    def reverseWords(self, s: str) -> str:
        words = s.split()
        new_words = []
        for word in words:
            new_word = self.reverse_string(list(word))
            new_words.append(new_word)
        return " ".join(new_words)


if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    print(Solution().reverseWords(s))

    s = "God Ding"
    print(Solution().reverseWords(s))
