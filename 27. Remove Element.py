class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ite = True
        
        while ite:
            if nums.count(val) >= 1: #val至少一個，移除val
                nums.remove(val)
            else:
                ite = False
        return len(nums)
