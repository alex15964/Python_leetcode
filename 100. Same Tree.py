# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None: #兩個都為None則相同
            return True
        elif p == None or q == None: #其中一個為None則不同
            return False
        elif p.val != q.val: #如果兩個值不同
            return False
        else: #如果相同則繼續往左跟往右跑
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
