class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if len(x) % 2 == 0: #如果是偶數字元，直接對半前後比較
            fx = x[0:int(len(x)/2)]
            bx = x[-1:int(len(x)/2-1):-1]
        else: #如果是奇數字元，去掉中間再對半前後比較
            fx = x[0:int(len(x)/2 - 0.5)]
            bx = x[-1:int(len(x)/2 - 0.5):-1]
        if fx == bx:
            return True
        else:
            return False
