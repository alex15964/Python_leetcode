class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack: #找出haystack中的needle位置
            return haystack.index(needle)
        else:
            return -1
