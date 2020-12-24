class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: #第一個給1
            return "1"
        
        pre = self.countAndSay(n-1) #recursion，取上一個的值
        ans = ""
        i = 0
        while i < len(pre): #開始取每個值做比較
            t = 1 #預設每個值至少1個
            for j in range(i, len(pre)-1): #從當前值往後比對到倒數第二個值為止
                if pre[j] == pre[j+1]: #當前值與下一值相同，次數+1
                    t += 1
                else: #只要不同就跳出
                    break
            ans += str(t) + pre[i] #答案為次數+當前值
            i += t #往後跳幾位(幾個相同)
        return ans
