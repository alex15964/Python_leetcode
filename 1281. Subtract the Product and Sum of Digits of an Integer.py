class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        dn = list(i for i in str(n))    #將數字轉字串再一一取出
        pd = 1  #預設相乘為1
        sd = 0  #預設相加為0
        for i in dn:    #相乘
            pd *= int(i)
            
        for i in dn:    #相加
            sd += int(i)
            
        return pd - sd
