class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target <= nums[i]: #當target小於等於當下位址的值，插入當下位址
                return i
        else: #如果都沒比自己小或等於的值，必定插入最後一位
            return len(nums)
