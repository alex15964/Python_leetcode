class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) > 0: #先判斷否nums是否為空
            outmax = nums[0] #先取第一值當作最大值
            inmax = 0 #每個排列組合最大先預設為0
            for n in nums:
                inmax += n #排列組合最大開始加
                inmax = max(n, inmax) #排列組合最大取加總前或加總後
                outmax = max(inmax, outmax) #最大值再判斷排列組合或當前值
            return outmax
        return 0
