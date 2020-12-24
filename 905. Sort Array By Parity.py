class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        ls = []
        for i in A: #每個值除以2，偶數塞前面，否則塞後面
            if i % 2 == 0:
                ls.insert(0, i)
            else:
                ls.append(i)
        return ls
