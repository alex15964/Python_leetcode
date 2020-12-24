class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        n = 0
        while n+1 < len(nums): #往下一個計算
            for i in range(nums[n]): #增加n個n+1
                ans.append(nums[n+1])
            n += 2
        return ans
