# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None: #如果到底層就回傳0
            return 0
        else:
            ldep = self.maxDepth(root.left) #recursive左跟右
            rdep = self.maxDepth(root.right)
            return max(ldep, rdep)+1 #往上爬一層就+1，選出左右中較深的Node
