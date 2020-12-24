class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            if target - num in nums: #減掉的數字是否也在nums
                if target - num != num: #確認兩數字是否相同
                    return [nums.index(num), nums.index(target - num)]
                elif nums.count(num) >= 2: #如果至少兩個同數字
                    return [nums.index(num), nums.index(num, nums.index(num) + 1)]
