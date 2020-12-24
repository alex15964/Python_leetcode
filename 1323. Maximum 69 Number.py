class Solution:
    def maximum69Number (self, num: int) -> int:
        ls = [i for i in str(num)] #先轉成字串串列
        for i in range(len(ls)): #從頭找第一個6轉成9就離開
            if ls[i] == '6':
                ls[i] = '9'
                break
        ans = int(''.join(ls)) #合併回數字
        return ans
