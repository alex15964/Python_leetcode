# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans = 0
    
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def bfs(node: TreeNode, parent: TreeNode, grantParent: TreeNode):
            if grantParent and grantParent.val % 2 == 0: #上上一個node存在且為偶數就相加
                self.ans += node.val
            if node.left: #有左或右node時，繼續往下找
                bfs(node.left, node, parent)
            if node.right:
                bfs(node.right, node, parent)
        bfs(root, None, None) #呼叫bfs
        return self.ans
