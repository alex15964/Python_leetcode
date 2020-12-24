class Solution:
    def reverse(self, x: int) -> int:
        if x == 0: #0直接回傳
            return x
        x = str(x) #轉成字串
        while x[-1] == '0': #反轉後開頭為0的需先剔除
            x = x[0:-1]
        if x[0] != '-': #如果是負數，從第二字元開始反轉，超過值就傳0
            x = int(x[::-1])
            return x if x < 2**31-1 else 0
        else: #正數則直接回傳，超過值就傳0
            x = int(x[0] + x[-1:0:-1])
            return x if x > -2**31 else 0
