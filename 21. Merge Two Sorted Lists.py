# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
            
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2: #先確認l1跟l2都不是空的
            if l1.val > l2.val: #以l1為主要LN，如果l1比較大，交換位置後將l1接到l2後面
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2) #Recursion，持續呼叫function直到其中一LN為空
        return l1 or l2 #回傳不為空的LN
