class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        iterating = True
        i = 1
        
        while iterating:
            if i < len(nums): #不用while i < len(nums)，因len(nums)會一直改變
                if nums[i-1] == nums[i]: #若後者跟前者相同，移除前者
                    nums.pop(i-1)
                else:
                    i += 1
            else:
                iterating = False
                
        return len(nums)
