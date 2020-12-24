class Solution:
    def romanToInt(self, s: str) -> int:
        rtn = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}  #羅馬轉數字用dict
        sumn = 0
        n = 0 #取每字元用
        while n < len(s):
            if n+1 < len(s) and rtn[s[n+1]] > rtn[s[n]]: #如果還有下一位字元，且下一位比自己大
                sumn += rtn[s[n+1]] - rtn[s[n]] #則下一位減掉當前總和
                n += 2 #直接跳兩位
            else: #否則只加一位字元
                sumn += rtn[s[n]]
                n += 1
        return sumn
