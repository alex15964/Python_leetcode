class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[1]*n
        for i in range(n):
            if n-i > 1:
                dp[i] = dp[i-1]+dp[i-2] #每個當前數字解法，會是前一(-1)跟前二(-2)的解法總和
            else:
                dp[i] = dp[i-1] #因第一解法由2開始(1解法為1，已是dp內值)，跑到倒數第一值已是n
        return(dp[-1])
