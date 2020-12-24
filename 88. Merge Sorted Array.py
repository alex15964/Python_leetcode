class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1l = len(nums1)
        while n1l - m > 0: #nums1存的值比m還多時就pop
            nums1.pop(-1)
            m += 1
        
        n2l = len(nums2)
        while n2l - n > 0: #nums2存的值比n還多時就pop
            nums2.pop(-1)
            n += 1
            
        nums1.extend(nums2) #合併並排序
        nums1.sort()
