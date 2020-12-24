# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root != None: #先判斷是否為空，如不是則將tree切成左右兩段
            return self.isMirror(root.left, root.right)
        else: #如果為空必定對稱
            return 1
    
    def isMirror(self, ln: TreeNode, rn: TreeNode) -> bool: #接收左邊跟右邊兩個tree
        if ln == None and rn == None: #左右皆空則為True
            return True
        elif ln == None or rn == None: #左右只有其中一個空則為False
            return False
        else:
            return ln.val == rn.val and self.isMirror(ln.left, rn.right) and self.isMirror(ln.right, rn.left) #比較當前值、左Tree的左跟右tree的右，和左tree的右跟右tree的左
