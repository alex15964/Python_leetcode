# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        value = 0
        exp = []
        while head != None: #先拆解lis
            exp.append(head.val)
            head = head.next
            
        for i in range(len(exp)):
            if exp[len(exp) - i - 1] == 1: #從尾到頭計算
                value += 2**i
            else:
                continue
        
        return value
