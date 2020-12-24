class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        while len(s) > 0 and s[-1] == ' ': #s至少一個值且最後一位為空格，去掉最後一位
            s = s[: -1]
            
        if len(s) == 0: #如果s空了回傳0
            return 0
        else:   #否則切割後回傳最後一個值
            sl = s.split(' ')
            return len(sl[-1])
