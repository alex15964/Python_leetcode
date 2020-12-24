# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        c = head
        while c and c.next: #當前跟下一個不為空時
            if c.val == c.next.val: #當前的值等於下一個的值時，下一個換成下下一個
                c.next = c.next.next
            else: #否則進位前往下一個
                c = c.next
        return head #c.next跟c.val操作為head底下記憶體同值，c本身操作則為複製操作
